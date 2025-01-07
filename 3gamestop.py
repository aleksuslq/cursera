import yfinance as yf

# Извлечение данных по акциям GameStop
gme_data = yf.download("GME", start="2020-01-01", end="2023-12-31")

# Сброс индекса
gme_data.reset_index(inplace=True)

# Отображение первых пяти строк датафрейма
print(gme_data.head())
