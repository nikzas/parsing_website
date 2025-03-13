import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Загрузка объединенного файла
df = pd.read_csv(r'D:\ProjectPython\parsing_website\csv\2024-07-25.csv')

# Получение общей информации о данных
print(df.info())
print(df.describe())
print(df.isnull().sum())  # Проверка на пропущенные значения


# Пример визуализации
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Value')  # Замените 'Value' на имя вашего столбца
plt.title('Числовой ряд по датам')
plt.xticks(rotation=45)
plt.show()

from statsmodels.tsa.stattools import adfuller

# Проверка стационарности временного ряда
result = adfuller(df['Value'])  # Замените 'Value' на имя вашего столбца
print('ADF Statistic:', result[0])
print('p-value:', result[1])