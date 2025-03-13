import ast
import pandas as pd
import numpy as np


def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [ast.literal_eval(line.strip()) for line in lines]


def find_shift_position(main_arr, new_arr, precision=2):
    if main_arr.size == 0 or new_arr.size == 0:
        return 0

    main_rounded = np.round(main_arr, precision)
    new_rounded = np.round(new_arr, precision)

    max_overlap = 0
    for possible_overlap in range(1, min(len(new_arr), len(main_arr)) + 1):
        if np.array_equal(new_rounded[-possible_overlap:], main_rounded[:possible_overlap]):
            max_overlap = possible_overlap

    return len(new_arr) - max_overlap


file_path = r'D:\ProjectPython\parsing_website\st\2025-02-27.txt'
output_csv_file = r'D:\ProjectPython\parsing_website\csv\2025-02-27.csv'

data = read_data(file_path)
if not data:
    print("Файл не содержит данных!")
    exit()

# Проверка одинаковой длины списков
list_length = len(data[0])
for idx, lst in enumerate(data):
    if len(lst) != list_length:
        print(f"Ошибка: список {idx} имеет длину {len(lst)} вместо {list_length}!")
        exit()

combined = np.array(data[0], dtype=np.float64)
print(f"Начальная длина: {len(combined)}")

for idx, lst in enumerate(data[1:]):
    new_arr = np.array(lst, dtype=np.float64)
    shift_pos = find_shift_position(combined, new_arr)
    print(f"Обработка списка {idx + 1}: добавляем {shift_pos} элементов")
    if shift_pos > 0:
        combined = np.concatenate([new_arr[:shift_pos], combined])

# Сохранение в CSV
pd.DataFrame(combined, columns=["Value"]).to_csv(output_csv_file, index=False)
print(f"Итоговая длина: {len(combined)}. Данные сохранены в {output_csv_file}")