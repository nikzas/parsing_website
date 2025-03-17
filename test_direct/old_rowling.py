import pandas as pd
import numpy as np

# Загрузка данных
df = pd.read_csv(r'D:\ProjectPython\parsing_website\test_direct\dataset\result.csv')
data = df.drop(columns='Time').values  # Убираем столбец времени

new_numbers = []
previous_row = None

for current_row in data:
    if previous_row is not None:
        # Находим смещение: ищем, с какого индекса текущая строка совпадает с предыдущей
        match_start = None
        for i in range(len(current_row)):
            # Проверяем совпадение оставшихся элементов
            if np.array_equal(current_row[i:], previous_row[:len(current_row)-i]):
                match_start = i
                break
        if match_start is not None:
            # Новые числа — первые 'match_start' элементов текущей строки
            new_numbers.extend(current_row[:match_start])
    previous_row = current_row

print("Новые числа:", new_numbers)
print(len(new_numbers))
