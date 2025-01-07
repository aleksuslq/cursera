import yfinance as yf

# Извлечение данных по акциям Tesla
tesla_data = yf.download("TSLA", start="2020-01-01", end="2023-12-31")

# Сброс индекса
tesla_data.reset_index(inplace=True)

# Отображение первых пяти строк датафрейма
print(tesla_data.head())
