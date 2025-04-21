import pandas as pd

file_path = "Копия Тестовые задания BPAD.xlsx"
xls = pd.ExcelFile(file_path)

df = xls.parse('Retention', header=None)

retention_values = df.iloc[7, 1:14].astype(float).tolist()
retention_values.insert(0, 1.0)

months = df.iloc[11:21, 0].tolist()
new_users = df.iloc[11:21, 1].astype(int).tolist()

october_mau = 0
for i in range(9):
    retention_month = 9 - i
    october_mau += new_users[i] * retention_values[retention_month]

october_mau += new_users[9] * retention_values[0]

october_mau = round(october_mau)

print("Прогноз MAU на октябрь 2021:", october_mau)
