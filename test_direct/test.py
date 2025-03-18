import csv
import os
from glob import glob

directory = r'D:\ProjectPython\parsing_website\test_direct\dataset'


def process_files():

    for filepath in glob(os.path.join(directory, '*.txt')):
        errors = {
            'not_line': 0,
            'fetch_error': 0,
            '-': 0,
            'max_values': 0,
            'min_values': 0
        }

        data = {}  # Словарь для хранения данных для текущего файла
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().replace('\xa0', '')

                if not line:
                    errors['not_line'] += 1  # Для подсчета ошибок
                    continue

                if 'Error fetching data' in line:
                    errors['fetch_error'] += 1  # Для подсчета ошибок
                    continue

                if ' - ' not in line:
                    errors['-'] += 1  # Для подсчета ошибок
                    continue

                time_part, values_part = line.split(' - ', 1)
                values = values_part.rstrip('x').split('x')

                if 5 < len(values) <= 20:
                    data[time_part] = values  # Сохраняем только 5-20 значений

                if len(values) < 20:
                    errors['max_values'] += 1
                    continue

                if 5 < len(values) :
                    errors['min_values'] += 1
                    continue

        # Очистка от повторяющихся значений
        filtered_data = clear_rows(data)

        print(f"Errors for {os.path.basename(filepath)}: {errors}")
        write_csv_file(filepath, filtered_data)  # Записываем в CSV файл с тем же именем
        errors.clear()

    return errors


def clear_rows(data):
    ### Очистка от повторяющихся словарей
    filtered = {}
    prev_values = None

    for time, values in data.items():
        if values != prev_values:
            filtered[time] = values
            prev_values = values
    return filtered


def write_csv_file(input_file, data):
    ### Генерация имени выходного файла
    output_file = os.path.splitext(input_file)[0] + '.csv'

    ### Запись в файл
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Time'] + [f'Value {i + 1}' for i in range(20)])  # Фиксированные 20 колонок
        for time, values in data.items():
            writer.writerow([time] + values)

    print(f"[Результат] Записано строк: {len(data)} в файл {output_file}")


if __name__ == '__main__':
    errors = process_files()
    print(errors)