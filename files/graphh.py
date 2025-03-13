import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf

# Загрузка данных
data = pd.read_csv(r"C:\project\parsing_website\csv\2024-07-26.csv", columns=["Value"])  # если есть время

# Гистограмма
plt.hist(data["Value"], bins=[1, 2, 3, 4, 5, 10, 100, 2000], edgecolor="black")
plt.yscale("log")  # для удобства, если есть экстремальные значения
plt.title("Распределение значений")
plt.show()

# Автокорреляция (лаги = 10)
autocorr = acf(data["Value"], nlags=10)
plt.stem(autocorr)
plt.title("Автокорреляция")
plt.show()

# Анализ экстремальных значений
high_values = data[data["Value"] > 100]
print("Экстремальные значения:", high_values["Value"].unique())
print("Их количество в день:", high_values.groupby(high_values["Time"].dt.date).size())