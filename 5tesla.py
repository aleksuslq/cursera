import yfinance as yf
import matplotlib.pyplot as plt

# Функция для построения графика
def make_graph(data, title):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label="Цена закрытия", color='blue')
    plt.title(title, fontsize=16)
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Цена (USD)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Загрузка данных по акциям Tesla
tesla_data = yf.download("TSLA", start="2020-01-01", end="2023-12-31")
tesla_data.reset_index(inplace=True)

# Построение графика
make_graph(tesla_data, "График акций Tesla (2020-2023)")
