import pandas as pd


df = pd.read_csv(r'D:\ProjectPython\parsing_website\test_direct\dataset\result.csv')
df.drop(columns=['Time'], inplace=True)

result = []
current_target = df.iloc[0, 0]
result.append(current_target)

for i in range(1, len(df)):
    row = df.iloc[i].tolist()
    try:
        idx = row.index(current_target)
        if idx > 0:
            result.append(row[idx-1])
            current_target = row[idx-1]
        # Если idx == 0, просто продолжаем без добавления
    except ValueError:
        # current_target не найден, продолжаем
        pass  # Ничего не делаем

print("Результат:", result)