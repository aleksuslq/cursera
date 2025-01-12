import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы с данными о доходах Tesla
url = "https://finance.yahoo.com/quote/TSLA/financials"

# Отправка HTTP-запроса на сайт
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    print("Данные успешно получены!")
else:
    print(f"Ошибка при загрузке страницы: {response.status_code}")

# Анализ HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Извлечение таблиц с финансовыми данными
data = []
headers = []

# Найдем таблицы на странице
tables = soup.find_all("table")

if tables:
    # Выбираем первую таблицу (обычно это таблица доходов)
    table = tables[0]

    # Извлечение заголовков таблицы
    header_row = table.find("thead")
    for header in header_row:
        headers.append(header.text.strip())

    # Извлечение строк данных
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        data.append([col.text.strip() for col in columns])
else:
    print("Таблицы не найдены.")

# Создание DataFrame из данных
df = pd.DataFrame(data, columns=headers)
print(df)

# Сохранение данных в CSV
df.to_csv("tesla_financials.csv", index=False)
print("Данные сохранены в файл tesla_financials.csv")
