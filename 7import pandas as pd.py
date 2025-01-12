import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Пример загрузки данных (замените на свои данные)
# Загрузите ваши данные в формате CSV
data = pd.read_csv("housing.csv")  # Укажите свой файл данных

# Список признаков для модели
features = [
    "floors", "waterfront", "lat", "bedrooms", "sqft_basement",
    "view", "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"
]

# Целевая переменная
target = "price"

# Удаляем строки с пропущенными значениями (если есть)
data = data.dropna(subset=features + [target])

# Разделение данных на признаки (X) и целевую переменную (y)
X = data[features]
y = data[target]

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Вывод результатов
print("Среднеквадратичная ошибка (MSE):", mse)
print("Коэффициент детерминации (R²):", r2)

# Коэффициенты модели
print("\nКоэффициенты линейной регрессии:")
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef}")
