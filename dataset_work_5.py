import pandas as pd
import numpy as np

#ЗАДАНИЕ 1

df = pd.read_csv("tested.csv")

total_miss = df.isnull().sum().sum()
column_miss = df.isnull().sum()
print("Всего пропусков:", total_miss)
print("\nПропусков по столбцам:")
print(column_miss)


print("\nТипы данных:")
print(df.dtypes)


numeric = df.select_dtypes(include=[np.number]).columns.tolist()
categorical = df.select_dtypes(exclude=[np.number]).columns.tolist()
print(f"\nЧисловые столбцы: {numeric}")
print(f"Текстовые столбцы: {categorical}")

#первые и последние 3 строки
n = 3
print(f"\nПервые {n} строки:")
print(df.head(n))
print(f"\nПоследние {n} строки:")
print(df.tail(n))

#статистика по возрасту 
col = 'Age'
if col in df.columns:
    print(f"\nСтатистика по '{col}':")
    print(df[col].describe())
else:
    print(f"\nСтолбец '{col}' не найден.")

#сколько строк и столбцов
print(f"\nСтолбцов: {df.shape[1]}")
print(f"Строк с данными: {df.shape[0]}")
print(f"Всего строк в файле (включая шапку): {df.shape[0] + 1}")



# пропуски в Age медианой (среднее значение по возрасту)
if 'Age' in df.columns:
    median_age = df['Age'].median()  
    df['Age'] = df['Age'].fillna(median_age)  #подставим вместо NaN
    print(f"\nВозраст заполнен медианой: {median_age:.1f}")


df_orig = pd.read_csv("tested.csv")
rows_with_nan = df_orig[df_orig.isnull().any(axis=1)]  #строки с пропусками

if len(rows_with_nan) >= 20:
    to_drop = rows_with_nan.index[:20]  #первые 20 таких строк
    df_clean = df_orig.drop(to_drop).reset_index(drop=True)
    print("\nУдалено 20 строк с пропусками.")
else:
    print(f"\nМеньше 20 строк с пропусками — удалено {len(rows_with_nan)} строк.")
    df_clean = df_orig.dropna().reset_index(drop=True)

# остатки
print(f"\nПосле удаления:")
print(f"Строк: {len(df_clean)}")
print(f"Пропусков: {df_clean.isnull().sum().sum()}")
print("\nПример (первые 3 строки):")
print(df_clean.head(3))

#ЗАДАНИЕ 2
import pandas as pd
import numpy as np

# Читаем файл
df = pd.read_csv("tested.csv")

# 1) Сравниваем Мужчин и Женщин

# a. Процент выживших
print("\n--- 1a. Процент выживших ---")
survived_by_sex = df.groupby('Sex')['Survived'].mean() * 100
print(survived_by_sex)

# b. Средний возраст
print("\n--- 1b. Средний возраст ---")
avg_age_by_sex = df.groupby('Sex')['Age'].mean()
print(avg_age_by_sex)

# c. Средний возраст выживших и погибших (по полу)
print("\n--- 1c. Средний возраст выживших/погибших по полу ---")
avg_age_survived = df.groupby(['Sex', 'Survived'])['Age'].mean()
print(avg_age_survived)

# 2) Фильтрация

# a. Старше 30, Мужчины, 1 класс
print("\n--- 2a. Старше 30, Мужчины, 1 класс ---")
filter_a = df[(df['Age'] > 30) & (df['Sex'] == 'male') & (df['Pclass'] == 1)]
print(f"Нашлось: {len(filter_a)} человек")
print(filter_a.head())  # первые 5 строк

# b. Моложе 18 ИЛИ женщины, которые выжили
print("\n--- 2b. Моложе 18 ИЛИ женщины, выжившие ---")
filter_b = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]
print(f"Нашлось: {len(filter_b)} человек")
print(filter_b.head())

# 3) Группировка по классу и полу

print("\n--- 3. Группировка по Pclass и Sex ---")
grouped = df.groupby(['Pclass', 'Sex'])

# a. Средний возраст
print("\na. Средний возраст:")
print(grouped['Age'].mean())

# b. Доля выживших
print("\nb. Доля выживших (%):")
print(grouped['Survived'].mean() * 100)

# c. Средняя стоимость билета
print("\nc. Средняя цена билета:")
print(grouped['Fare'].mean())
