import random

class Player:
    #стартовые параметры игрока(местонахождение, здоровье, наличие предметов и ключа)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []
        self.has_key = False
        self.health = 100
    #генерация лабиринта и перемещение по нему
    def move(self, dx, dy, maze_width, maze_height):
        new_x = self.x + dx
        new_y = self.y + dy
        #если игрок выходит на рамки поля
        if 0 <= new_x < maze_width and 0 <= new_y < maze_height:
            self.x = new_x
            self.y = new_y
            return True
        else:
            print("Вы врезались в стену!")
            return False
    #добавление предметов (append)
    def add_item(self, item):
        self.inventory.append(item)
        print("Добавлен предмет: " + str(item))
        if item == "волшебный ключ":
            self.has_key = True
    
    def add_items(self, items):
        # пакетное добавление (extend)
        self.inventory.extend(items)
        print("Добавлено несколько предметов: " + str(items))
        if "волшебный ключ" in items:
            self.has_key = True
    #удаление предметов(ключ нельзя удалять)
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print("Удален предмет: " + str(item))
            if item == "волшебный ключ":
                self.has_key = False
            return True
        return False
    #удаляем последний элемент через pop
    def use_last_item(self):
        if self.inventory:
            item = self.inventory.pop()
            print("Использован последний предмет: " + str(item))
            if item == "волшебный ключ":
                self.has_key = False
            return item
        return None
    
    def sort_inventory(self):
        #сортировка по длине названия предмета (lambda + sort)
        self.inventory.sort(key=lambda x: len(x))
        print("Инвентарь отсортирован по длине названия.")
    
    def reverse_inventory(self):
        self.inventory.reverse()
        print("Инвентарь перевернут (reverse).")
    #индексация предметов в инвентаре
    def find_item_index(self, item): 
        try:
            idx = self.inventory.index(item) #предмет найден
            print("Предмет '" + str(item) + "' найден в позиции " + str(idx))
            return idx
        except ValueError: #предмет не найден(через исключения)
            print("Предмет '" + str(item) + "' не найден в инвентаре.")
            return -1
     
    def has_item(self, item):
        if item in self.inventory:
            print("У вас есть: " + str(item))
            return True
        else:
            print("У вас нет: " + str(item))
            return False
    #вычетание значения из здоровья при получение урона от моба
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print("Получено урона: " + str(amount) + ". Здоровье: " + str(self.health))
        return self.health > 0


class Maze:
    #обозначения на карте
    ROOM_TYPES = {
        'empty': '.',
        'chest': 'C',
        'trap': 'T',
        'monster': 'M',
        'key': 'K',
        'portal': 'P'
    }
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.visited = []       # для «тихой карты» (открывается по мере прохождения)
        self.key_room = None
        self.portal_room = None
        self.generate_maze()
    
    def generate_maze(self):
        #сетка пустых комнат
        self.grid = [['empty' for _ in range(self.width)] for _ in range(self.height)]
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        #несколько специальных комнат
        rooms_to_place = [
            ('chest', 3),    # 3 сундука
            ('trap', 2),     # 2 ловушки (ядовое зелье, многоразовые)
            ('monster', 2),  # 2 монстра
        ]
        #заданные объекты генерируются на рандомных позициях при запуске программы
        for room_type, count in rooms_to_place:
            for _ in range(count):
                x, y = self.get_random_empty_position()
                self.grid[y][x] = room_type
        
        #размещаем ключ (уникальная комната)
        key_x, key_y = self.get_random_empty_position()
        self.grid[key_y][key_x] = 'key'
        self.key_room = (key_x, key_y)
        
        # размещаем портал (уникальная комната)
        portal_x, portal_y = self.get_random_empty_position()
        self.grid[portal_y][portal_x] = 'portal'
        self.portal_room = (portal_x, portal_y)
        
        # стартовая клетка помечается как посещённая
        self.visited[0][0] = True
    #отмечаем на карте открытые комнаты
    def mark_visited(self, x, y):
        self.visited[y][x] = True
    #определяем посещенные комнаты
    def is_visited(self, x, y):
        return self.visited[y][x]
    
    def get_random_empty_position(self):
        # Бесконечный цикл, который будет выполняться до тех пор, 
        # пока не будет найдена и возвращена подходящая позиция
        while True:
            # Генерируем случайную координату X в пределах поля
        # randint(a, b) возвращает случайное целое число
            x = random.randint(0, self.width - 1)
            # Генерируем случайную координату Y в пределах поля
        # randint(a, b) возвращает случайное целое число
            y = random.randint(0, self.height - 1)
            #условия: позиция не стартовая 
            if self.grid[y][x] == 'empty' and (x != 0 or y != 0):  #не стартовая позиция
                return x, y
    #генерация типа комнаты
    def get_room_type(self, x, y):
        return self.grid[y][x]
    
    def display(self, player_x, player_y, quiet=True):
        # quiet=True — «тихая карта»: непосещённые клетки показываются как '?'
        print("\n" + "=" * (4 * self.width))
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == player_x and y == player_y: #команата открыта 
                    row.append("@")
                else:
                    if quiet and not self.is_visited(x, y): #комната закрыта
                        row.append("?")
                    else:
                        room_type = self.grid[y][x]
                        row.append(self.ROOM_TYPES[room_type])
            print(" ".join(row))
        print("=" * (4 * self.width))


class Game:
    def __init__(self, width=5, height=5):
        self.maze = Maze(width, height)
        self.player = Player(0, 0)  # старт в левом верхнем углу
        self.game_over = False
        self.win = False
    
    def handle_room_event(self):
        # помечаем клетку посещённой при входе
        self.maze.mark_visited(self.player.x, self.player.y)
        room_type = self.maze.get_room_type(self.player.x, self.player.y)
        
        if room_type == 'empty':
            print("Пустая комната. Ничего не происходит.")
        
        elif room_type == 'chest':
            # иногда выдаем несколько предметов для extend
            single_treasures = ["золотая монета", "магический кристалл", "древний свиток", "серебряный кулон"]
            bundle_treasures = [["монета", "камень удачи"], ["свиток огня", "зелье лечения"]]
            if random.random() < 0.5:
                treasure = random.choice(single_treasures)
                print("Вы нашли сундук! Получен предмет: " + str(treasure))
                self.player.add_item(treasure)  
            else:
                items = random.choice(bundle_treasures) #предметы в сундуке рандомные
                print("Вы нашли сундук! Получены предметы: " + str(items))
                self.player.add_items(items)    
            #сундук становится пустой комнатой после использования
            self.maze.grid[self.player.y][self.player.x] = 'empty'
        
        elif room_type == 'trap':
            print("Вы наступили на ядовитую ловушку. Минус 20 здоровья.")
            if not self.player.take_damage(20):
                print("Вы погибли от яда.")
                self.game_over = True
            else:
                print("Ловушка многоразовая и остается на месте.")
        
        elif room_type == 'monster':
            print("На вас напал монстр. Минус 30 здоровья.")
            if not self.player.take_damage(30): #если урон больше здоровья игрока 
                print("Вы были побеждены монстром.")
                self.game_over = True
            else:
                print("Монстр отступил, но остается в комнате.")
        
        elif room_type == 'key':
            print("Вы нашли волшебный ключ. Теперь можно активировать портал.")
            self.player.add_item("волшебный ключ")
            self.maze.grid[self.player.y][self.player.x] = 'empty'
        #чтобы активировать портал нужен ключ
        elif room_type == 'portal':
            if self.player.has_key:
                print("Вы используете ключ и активируете портал. Победа!")
                self.win = True
                self.game_over = True
            else:
                print("Это портал-выход, но у вас нет ключа.")
    #просмотр статуса игрока
    def show_status(self):
        print("\nПозиция: (" + str(self.player.x) + ", " + str(self.player.y) + ")")
        print("Здоровье: " + str(self.player.health))
        print("Инвентарь (" + str(len(self.player.inventory)) + "): " + str(self.player.inventory))
        print("Ключ: " + ("есть" if self.player.has_key else "нет"))
    
    def demonstrate_collections_operations(self):
        print("\n" + "="*50)
        print("операции по спикам (Python)")
        print("="*50)
        
        # 1. append, extend — добавление элементов
        print("\n1) Добавление элементов (append, extend):")
        demo_list = ["предмет1", "предмет2"]
        print("Начальный список: " + str(demo_list))
        demo_list.append("новый предмет")        # append
        print("После append: " + str(demo_list))
        demo_list.extend(["доп1", "доп2"])       # extend
        print("После extend: " + str(demo_list))
        
        # 2. remove, pop — удаление элементов
        print("\n2) Удаление элементов (remove, pop):")
        demo_list.remove("предмет1")             # remove
        print("После remove('предмет1'): " + str(demo_list))
        popped = demo_list.pop()                 # pop
        print("После pop(): удален '" + str(popped) + "', список: " + str(demo_list))
        
        # 3. сортировка с lambda, sort, reverse
        print("\n3) Сортировка (lambda, sort, reverse):")
        items = ["зелье", "меч", "кольцо", "щит"]
        print("До сортировки: " + str(items))
        items.sort(key=lambda x: len(x))         # sort с lambda
        print("После сортировки по длине: " + str(items))
        items.reverse()                           # reverse
        print("После reverse: " + str(items))
        
        # 4. поиск — index, in/not in
        print("\n4) Поиск элементов (index, in/not in):")
        print("'меч' в списке? " + str("меч" in items))     # in
        print("'лук' в списке? " + str("лук" in items))     # in
        print("Индекс 'щит': " + str(items.index("щит")))   # index
        
        # 5. Копирование и модификация — copy, slicing
        print("\n5) Копирование (copy, slicing):")
        original = ["A", "B", "C", "D"]
        copy1 = original.copy()   # copy
        copy2 = original[:]       # slicing
        copy1[0] = "X"
        copy2[1] = "Y"
        print("Оригинал: " + str(original))
        print("Копия (copy): " + str(copy1))
        print("Копия (slicing): " + str(copy2))
        
        print("\n(Возврат в игру...)\n")
    
    def player_actions(self):
        print("\nДоступные действия:")
        print("W / A / S / D - Двигаться")
        print("2. Показать инвентарь")
        print("3. Отсортировать инвентарь")
        print("4. Перевернуть инвентарь")
        print("5. Найти предмет в инвентаре (показать позицию)")
        print("6. Проверить наличие предмета")
        print("7. Выбросить предмет")
        print("8. Использовать последний предмет")
        print("9. Показать карту (тихая)")
        print("10. Показать обучение по спискам (Python)")
        print("0. Выйти из игры")
        
        choice = input("Выберите действие (или WASD): ").lower()
        
        if choice in ['w', 'a', 's', 'd']:
            moves = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}
            dx, dy = moves[choice]
            if self.player.move(dx, dy, self.maze.width, self.maze.height):
                # помечаем посещение и обрабатываем событие комнаты
                self.handle_room_event()
        
        elif choice == '2':
            print("\nИнвентарь: " + str(self.player.inventory))
        
        elif choice == '3':
            self.player.sort_inventory()
        
        elif choice == '4':
            self.player.reverse_inventory()
        
        elif choice == '5':
            item = input("Введите название предмета для поиска: ")
            self.player.find_item_index(item)
        
        elif choice == '6':
            item = input("Введите название предмета для проверки: ")
            self.player.has_item(item)
        
        elif choice == '7':
            item = input("Введите название предмета для удаления: ")
            if self.player.remove_item(item):
                print("Предмет удален.")
            else:
                print("Предмет не найден.")
        
        elif choice == '8':
            used_item = self.player.use_last_item()
            if used_item:
                print("Вы использовали: " + str(used_item))
            else:
                print("Инвентарь пуст.")
        
        elif choice == '9':
            # «тихая карта» — непосещённые клетки скрыты
            self.maze.display(self.player.x, self.player.y, quiet=True)
        
        elif choice == '10':
            self.demonstrate_collections_operations()
        
        elif choice == '0':
            self.game_over = True
        
        else:
            print("Неверный выбор.")
    
    def start(self):
        print("ДОБРО ПОЖАЛОВАТЬ В ЛАБИРИНТ!")
        print("Цель: найти ключ и добраться до портала (выхода).")
        print("Обозначения: @ - игрок, . - пусто, C - сундук, T - ловушка, M - монстр, K - ключ, P - портал")
        print("Непосещённые клетки показываются как '?'. Двигайтесь W/A/S/D. Старт: (0,0).\n")
        
        while not self.game_over:
            self.show_status()
            
            self.maze.display(self.player.x, self.player.y, quiet=True)
            self.player_actions()
            
            if self.player.health <= 0 and not self.game_over:
                self.game_over = True
                print("Игра окончена. Вы погибли.")
            
            if self.win:
                print("Поздравляю! Вы прошли лабиринт!")
        
        print("\nСпасибо за игру!")

if __name__ == "__main__":
    Game(5, 5).start()
