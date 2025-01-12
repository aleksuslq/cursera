import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

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

# Удаление пропущенных значений, если они есть
df.dropna(subset=["price", "sqft_living"], inplace=True)

# Создание массивов для модели
X = df[["sqft_living"]].values  # Преобразуем в 2D массив
y = df["price"].values          # Целевые значения

# Инициализация модели линейной регрессии
model = LinearRegression()

# Обучение модели
model.fit(X, y)

# Предсказание на обучающей выборке
y_pred = model.predict(X)

# Расчет R^2
r2 = r2_score(y, y_pred)

# Вывод результатов
print(f"Коэффициент R^2: {r2:.4f}")
print(f"Уравнение регрессии: price = {model.intercept_:.2f} + {model.coef_[0]:.2f} * sqft_living")
