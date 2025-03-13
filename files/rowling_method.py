import ast
import pandas as pd
import numpy as np
import os

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

input_folder = r'C:\project\parsing_website\st'
output_folder = r'C:\project\parsing_website\csv'

# Получаем список всех файлов в папке
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):  # Обрабатываем только файлы с расширением .txt
        file_path = os.path.join(input_folder, filename)
        output_csv_file = os.path.join(output_folder, filename.replace('.txt', '.csv'))

        data = read_data(file_path)
        if not data:
            print(f"Файл {filename} не содержит данных!")
            continue

        # Проверка одинаковой длины списков
        list_length = len(data[0])
        for idx, lst in enumerate(data):
            if len(lst) != list_length:
                print(f"Ошибка в файле {filename}: список {idx} имеет длину {len(lst)} вместо {list_length}!")
                break
        else:
            combined = np.array(data[0], dtype=np.float64)
            print(f"Начальная длина в файле {filename}: {len(combined)}")

            for idx, lst in enumerate(data[1:]):
                new_arr = np.array(lst, dtype=np.float64)
                shift_pos = find_shift_position(combined, new_arr)
                print(f"Обработка списка {idx + 1} в файле {filename}: добавляем {shift_pos} элементов")
                if shift_pos > 0:
                    combined = np.concatenate([new_arr[:shift_pos], combined])

            # Сохранение в CSV
            pd.DataFrame(combined, columns=["Value"]).to_csv(output_csv_file, index=False)
            print(f"Итоговая длина в файле {filename}: {len(combined)}. Данные сохранены в {output_csv_file}")