import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL с данными о доходах GameStop (например, Yahoo Finance)
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

# Отправка HTTP-запроса к странице
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Поиск таблицы с доходами
tables = soup.find_all("table")
if tables:
    # Преобразование первой таблицы в DataFrame
    gme_revenue = pd.read_html(str(tables[0]))[0]

    # Преобразование таблицы: первая строка как названия столбцов
    gme_revenue.columns = gme_revenue.iloc[0]
    gme_revenue = gme_revenue[1:]

    # Вывод последних пяти строк
    print(gme_revenue.tail())
else:
    print("Таблицы с данными не найдены на странице.")
