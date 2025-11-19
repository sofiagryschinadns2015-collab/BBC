import random
from collections import deque, OrderedDict

#       настройки эксперимента
BLOCK_SIZE = 16        # байт в строке кэша
CACHE_LINES_LIST = [4, 8, 16, 32, 64]
POLICIES = ["FIFO", "LRU", "Random"]
HIT_TIME = 1           # такт
MISS_PENALTY = 50      
random.seed(0)         # фиксируем начальное значение для воспроизводимости Random

#генераторы обращений
def trace_sum_array(n_elems=256, base=0x10000000, elem_size=4):
    
    return [("R", base + i*elem_size) for i in range(n_elems)]

def trace_bubble_sort(n_elems=64, base=0x20000000, elem_size=4):
    """
    пузырьковая сортировка (худший случай ):
    на каждой итерации читаем A[j], A[j+1], затем снова читаем и пишем их.
    возвращает список ("R"/"W", addr)
    """
    trace = []
    for i in range(n_elems):
        for j in range(n_elems - 1 - i):
            a = base + j*elem_size
            b = base + (j+1)*elem_size
            # сравнение
            trace.append(("R", a))
            trace.append(("R", b))
            # предположим, что своп всегда происходит 
            trace.append(("R", a))
            trace.append(("R", b))
            trace.append(("W", a))
            trace.append(("W", b))
    return trace

#политики вытеснения
def simulate_cache_fifo(trace, cache_lines, block_size):
    """
    FIFO: вытесняем самый старый блок
    """
    hits = 0
    misses = 0
    q = deque()       # порядок заселения: слева самый старый
    in_cache = set()  # проверяем наличие

    for _, addr in trace:
        block = addr // block_size
        if block in in_cache:
            hits += 1
        else:
            misses += 1
            if len(in_cache) >= cache_lines:
                victim = q.popleft()
                in_cache.remove(victim)
            in_cache.add(block)
            q.append(block)
    return hits, misses

def simulate_cache_lru(trace, cache_lines, block_size):
    """
    LRU: вытесняем наименее недавно использованный блок
    """
    hits = 0
    misses = 0
    od = OrderedDict()  

    for _, addr in trace:
        block = addr // block_size
        if block in od:
            hits += 1
            od.move_to_end(block)  # стал самым свежим
        else:
            misses += 1
            if len(od) >= cache_lines:
                od.popitem(last=False)  # убрать LRU (левый)
            od[block] = None
    return hits, misses

def simulate_cache_random(trace, cache_lines, block_size):
    """
    Random:  выбираем жертву случайно
    """
    hits = 0
    misses = 0
    arr = []     # список блоков в кэше
    in_cache = set()

    for _, addr in trace:
        block = addr // block_size
        if block in in_cache:
            hits += 1
        else:
            misses += 1
            if len(arr) >= cache_lines:
                victim = random.choice(arr)
                arr.remove(victim)
                in_cache.remove(victim)
            arr.append(block)
            in_cache.add(block)
    return hits, misses

# выбор политики по имени ---
def simulate_cache(trace, cache_lines, block_size, policy):
    if policy == "FIFO":
        return simulate_cache_fifo(trace, cache_lines, block_size)
    elif policy == "LRU":
        return simulate_cache_lru(trace, cache_lines, block_size)
    elif policy == "Random":
        return simulate_cache_random(trace, cache_lines, block_size)
    else:
        raise ValueError(f"Unknown policy: {policy}")

# посчитаем hits/misses, hit_rate и AMAT 
def evaluate(trace, workload_name):
    total = len(trace)
    rows = []
    for cl in CACHE_LINES_LIST:
        for pol in POLICIES:
            hits, misses = simulate_cache(trace, cl, BLOCK_SIZE, pol)
            hit_rate = hits / total
            miss_rate = 1 - hit_rate
            amat = HIT_TIME + miss_rate * MISS_PENALTY
            rows.append({
                "workload": workload_name,
                "cache_lines": cl,
                "policy": pol,
                "hits": hits,
                "misses": misses,
                "hit_rate": hit_rate,
                "AMAT_cycles": amat
            })
    return rows

# печать  таблицы в консоль 
def print_table(rows, title):
    print("\n" + title)
    print("-" * len(title))
    header = f"{'cache_lines':>11}  {'policy':>8}  {'hits':>7}  {'misses':>7}  {'hit_rate':>9}  {'AMAT':>8}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(f"{r['cache_lines']:>11}  {r['policy']:>8}  {r['hits']:>7}  {r['misses']:>7}  "
              f"{r['hit_rate']*100:>8.3f}%  {r['AMAT_cycles']:>8.4f}")
    print()

def main():
    #генерируем данные для тестирования
    sum_trace = trace_sum_array()
    bubble_trace = trace_bubble_sort()

    # проверка длин (должно быть 256 и 12096)
    # print(len(sum_trace), len(bubble_trace))

    
    sum_rows = evaluate(sum_trace, "sum_array")
    bubble_rows = evaluate(bubble_trace, "bubble_sort")

    
    sum_only = [r for r in sum_rows if r["workload"] == "sum_array"]
    bubble_only = [r for r in bubble_rows if r["workload"] == "bubble_sort"]

    #консольные таблицы 
    print_table(sum_only, "SumArray — результаты")
    print_table(bubble_only, "BubbleSort — результаты")

    # Опционально: pandas/matplotlib
    try:
        import pandas as pd
        import matplotlib.pyplot as plt

        df = pd.DataFrame(sum_rows + bubble_rows)
        df.to_csv("results.csv", index=False)
        print("CSV сохранён: results.csv")

        # графики по BubbleSort: hit rate и AMAT
        bdf = df[df["workload"] == "bubble_sort"].copy()

        plt.figure()
        for pol in POLICIES:
            sub = bdf[bdf["policy"] == pol]
            plt.plot(sub["cache_lines"], sub["hit_rate"], marker="o", label=pol)
        plt.xlabel("Число строк кэша (по 16 байт)")
        plt.ylabel("Доля попаданий")
        plt.title("BubbleSort: Hit rate vs cache size")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig("hitrate_bubble.png", dpi=150, bbox_inches="tight")
        print("График сохранён: hitrate_bubble.png")

        plt.figure()
        for pol in POLICIES:
            sub = bdf[bdf["policy"] == pol]
            plt.plot(sub["cache_lines"], sub["AMAT_cycles"], marker="o", label=pol)
        plt.xlabel("Число строк кэша (по 16 байт)")
        plt.ylabel("AMAT (такты)")
        plt.title("BubbleSort: AMAT vs cache size")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig("amat_bubble.png", dpi=150, bbox_inches="tight")
        print("График сохранён: amat_bubble.png")

    except Exception as e:
        print(f"Построение графиков пропущено: {e}")
        if __name__ == "__main__":
            main()
