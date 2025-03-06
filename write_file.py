import os

def remove_consecutive_duplicates(list_of_lists):
    if not list_of_lists:
        return []

    result = [list_of_lists[0]]
    for current_list in list_of_lists[1:]:
        if current_list != result[-1]:
            result.append(current_list)
    return result

directory = r'D:\ProjectPython\parsing_website\st'

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    file_path = os.path.join(directory, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        numbers_list = []
        for line in f:
            if ' - ' in line and 'Error' not in line:
                data = line.split(' - ')[1].strip().replace('\xa0', '')
                numbers = [float(num)
                                for num in data.rstrip('x').split('x')
                                    if num and num != '0']
                if 5 <= len(numbers) <= 20:
                    numbers_list.append(numbers)

        numbers_list = remove_consecutive_duplicates(numbers_list)

        with open(file_path, 'w', encoding='utf-8') as f:
            for numbers in numbers_list:
                f.write(f"{numbers}\n")