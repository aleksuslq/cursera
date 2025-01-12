import pandas as pd
import requests

# Функция для загрузки файла
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

# Загрузка данных
filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
download(filepath, "housing.csv")

# Чтение CSV-файла
file_name = "housing.csv"
df = pd.read_csv(file_name)

# Подсчет количества домов с уникальными значениями в колонке "floors"
floor_counts = df["floors"].value_counts()

# Преобразование в DataFrame
floor_counts_df = floor_counts.to_frame(name="count")

# Переименование индекса
floor_counts_df.index.name = "floors"

# Вывод результата
print(floor_counts_df)
