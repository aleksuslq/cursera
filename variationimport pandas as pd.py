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

# Загрузка данных
filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
download(filepath, "housing.csv")

# Чтение CSV-файла
file_name = "housing.csv"
df = pd.read_csv(file_name)

# Построение boxplot для анализа ценовых отклонений
plt.figure(figsize=(10, 6))
sns.boxplot(x="waterfront", y="price", data=df)
plt.title("Price Variation for Waterfront and Non-Waterfront Homes")
plt.xlabel("Waterfront (1 = Yes, 0 = No)")
plt.ylabel("Price")
plt.show()
