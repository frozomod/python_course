import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Задание 1
df1 = pd.DataFrame(np.random.randint(1, 11, size=(10, 10)))

print("DataFrame 1:")
print(df1)

# Задание 2
df1.index = list("ABCDEFGHIJ")
row_gt_5_values = df1[df1.apply(lambda row: all(row > 5), axis=1)]
if not row_gt_5_values.empty:
    print("\nСтрока с числами > 5:")
    print(row_gt_5_values.iloc[0])
else:
    print("\nНет строки, где все числа > 5.")

# Задание 3
df2 = pd.DataFrame(np.random.rand(10, 10))

df2.index = list("ABCDEFGHIJ")
df2.columns = list("abcdefghij")

print(f"\nРазмерность матрицы: {df2.shape}")

print(f"\nИндексы столбцов: {df2.columns}")

print(f"\nСреднее значение матрицы: {df2.values.mean()}")

df2.to_csv("matrix.csv", index=False)
print("\nМатрица записана в файл 'matrix.csv'")

# Задание 4

df_emojis = pd.read_csv('emojis.csv')

df_sorted = df_emojis.sort_values(by='Rank', ascending=True)

print("Отсортированный DataFrame:")
print(df_sorted.head())

most_popular_subcategory = df_sorted['Subcategory'].iloc[0]
print(f"\nСамая популярная подкатегория эмоджи: {most_popular_subcategory}")

# Задание 5
df_emojis = pd.read_csv('emojis.csv')

df_emojis['Year'] = pd.to_datetime(df_emojis['Year'], format='%Y')

emojis_per_year = df_emojis.groupby(df_emojis['Year'].dt.year).size()

plt.figure(figsize=(10, 6))
emojis_per_year.plot(kind='bar', color='skyblue')
plt.title('Количество созданных эмоджи за каждый год')
plt.xlabel('Год')
plt.ylabel('Количество эмоджи')
plt.show()
