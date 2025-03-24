import pandas as pd
import numpy as np
import os
import glob

# Путь к папке с CSV файлами
input_folder = r'D:\ProjectPython\parsing_website\test_direct\csv_results\*.csv'
output_folder = r'D:\ProjectPython\parsing_website\test_direct\result_ready'


# Получаем список всех CSV файлов в папке
csv_files = glob.glob(input_folder)

for file in csv_files:
    df = pd.read_csv(file)

    data = df.drop(columns='Time').values
    time_column = df['Time'].values

    new_numbers = []
    time_new_numbers = []

    # Добавляем первое число из первой строки
    first_number = data[0][0]  # Первое число из первой строки
    new_numbers.append(first_number)
    time_new_numbers.append(time_column[0])  # Время для первого числа

    previous_row = data[0]  # Устанавливаем предыдущую строку как первую строку

    for index in range(1, len(data)):  # Начинаем с 1, так как 0 уже обработано
        current_row = data[index]
        # Находим смещение: ищем, с какого индекса текущая строка совпадает с предыдущей
        match_start = None
        for i in range(len(current_row)):
            # Проверяем совпадение оставшихся элементов
            if np.array_equal(current_row[i:], previous_row[:len(current_row) - i]):
                match_start = i
                break
        if match_start is not None:
            # Получаем сегмент новых чисел
            segment = current_row[:match_start].tolist()
            new_numbers.extend(segment[::-1])
            # Добавляем соответствующее время
            time_new_numbers.extend([time_column[index]] * len(segment[::-1]))

        previous_row = current_row  # Обновляем предыдущую строку

    # Создаем новый DataFrame с временем и новыми числами
    result_df = pd.DataFrame({
        'Time': time_new_numbers,
        'New Numbers': new_numbers
    })

    # Формируем имя выходного файла
    output_file = os.path.join(output_folder, os.path.basename(file))

    # Запись результатов в файл
    result_df.to_csv(output_file, index=False)

    print(f"Обработан файл: {file}, сохранен как: {output_file}")

