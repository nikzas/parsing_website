import csv
import os
from glob import glob

directory = r'D:\ProjectPython\parsing_website\test_direct\dataset'
output_file = r'D:\ProjectPython\parsing_website\test_direct\dataset\2024-07-25.csv'


def process_files():
    data = {}
    errors = {
        'invalid_format': 0,
        'fetch_error': 0,
        'min_values': 0,
        'max_values': 0
    }

    for filepath in glob(os.path.join(directory, '*.txt')):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().replace('\xa0', '')

                if not line or 'Error fetching data' in line or ' - ' not in line:
                    errors['invalid_format'] += 1 # Для подсчета ошибок
                    continue

                time_part, values_part = line.split(' - ', 1)
                values = values_part.rstrip('x').split('x')

                if 5 < len(values) <= 20:
                    data[time_part] = values  # Сохраняем только 5-20 значений
    print(errors)
    return data


def clear_rows(data):
    ### Очистка от повторяющихся словарей
    filtered = {}
    prev_values = None

    for time, values in data.items():
        if values != prev_values:
            filtered[time] = values
            prev_values = values
    return filtered


def write_csv_file(filter):
    ### Запись в файл
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Time'] + [f'Value {i + 1}' for i in range(20)])  # Фиксированные 20 колонок
        for time, values in filter.items():
            writer.writerow([time] + values)

    print(f"[Результат] Записано строк: {len(filter)}")


if __name__ == '__main__':
    data = process_files()
    data_set = clear_rows(data)
    write_csv_file(data_set)