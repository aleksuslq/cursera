import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL с данными о доходах Tesla (пример: на основе Yahoo Finance)
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

# Отправка запроса к веб-странице
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Извлечение таблицы с данными о доходах
tables = soup.find_all("table")
if tables:
    # Конвертация первой таблицы в DataFrame
    tesla_revenue = pd.read_html(str(tables[0]))[0]

    # Переименование столбцов для удобства
    tesla_revenue.columns = tesla_revenue.iloc[0]
    tesla_revenue = tesla_revenue[1:]

    # Вывод последних пяти строк
    print(tesla_revenue.tail())
else:
    print("None")
