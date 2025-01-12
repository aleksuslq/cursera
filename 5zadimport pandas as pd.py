import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# Функция для загрузки файла
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(f"Не удалось загрузить файл. Статус код: {response.status_code}")

# Загрузка данных
filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
download(filepath, "housing.csv")

# Чтение CSV-файла
file_name = "housing.csv"
df = pd.read_csv(file_name)

# Проверка первых строк DataFrame
print(df.head())

# Построение регрессионного графика
plt.figure(figsize=(10, 6))
sns.regplot(x="sqft_above", y="price", data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title("Влияние площади над землей (sqft_above) на цену дома")
plt.xlabel("Площадь над землей (sqft_above)")
plt.ylabel("Цена дома (price)")
plt.show()
