import ast

# Функция для чтения данных из файла
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Преобразуем строки в списки чисел
    return [ast.literal_eval(line.strip()) for line in lines]

# Основная логика обработки данных
def process_data(data):
    # Инициализация основного списка с первой строкой
    main_list = data[0]

    # Обработка каждой последующей строки
    for i in range(1, len(data)):
        new_number = data[i][0]  # Первое число из текущей строки
        # Добавляем новое число в начало списка
        main_list.insert(0, new_number)

    return main_list

# Функция для записи списка в файл
def write_data(file_path, data):
    with open(file_path, 'w') as file:
        file.write(str(data))

# Путь к файлу
input_file_path = '../st/2024-07-25.txt'
output_file_path = '../output.csv'

# Чтение данных из файла
data = read_data(input_file_path)

# Обработка данных
main_list = process_data(data)

# Запись итогового списка в файл
write_data(output_file_path, main_list)

print(f"Итоговый список записан в файл: {output_file_path}")