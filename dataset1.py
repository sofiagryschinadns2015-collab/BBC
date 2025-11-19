import pandas as pd
import numpy as np

# Чтение данных
df = pd.read_csv("tested.csv")  # ← ИСПРАВЛЕНО: read_csv и .csv

# Пропуски
total_miss = df.isnull().sum().sum()
column_miss = df.isnull().sum()
print("всего пропусков:", total_miss)
print("\nпропусков по столбцам:")
print(column_miss)

# Первые и последние n строк
n = 3
print(f"\nпервые {n} строки:")
print(df.head(n))

print(f"\nпоследние {n} строки:")
print(df.tail(n))

# Базовая статистика по столбцу Age
column = 'Age'
if column in df.columns:
    print(f"\nбазовая статистика по столбцу '{column}':")
    print(df[column].describe())
else:
    print(f"\ncтолбец '{column}' не найден.")

# Количество столбцов и строк
num_columns = df.shape[1]
num_rows_data = df.shape[0]
print(f"\nКоличество столбцов (заголовков): {num_columns}")
print(f"Количество строк с данными: {num_rows_data}")
print(f"Общее количество строк в CSV-файле (данные + заголовок): {num_rows_data + 1}")