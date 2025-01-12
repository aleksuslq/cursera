import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

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

# Создание объекта конвейера
pipeline = Pipeline([
    ("scaler", StandardScaler()),               # Масштабирование данных
    ("poly", PolynomialFeatures(degree=2)),    # Полиномиальное преобразование
    ("model", LinearRegression())              # Линейная регрессия
])

# Обучение модели
pipeline.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = pipeline.predict(X_test)

# Вычисление R^2
r2 = r2_score(y_test, y_pred)
print(f"Коэффициент детерминации (R²): {r2:.4f}")
