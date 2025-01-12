from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

# Полиномиальное преобразование второго порядка
poly = PolynomialFeatures(degree=2)

# Преобразование обучающих и тестовых данных
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Масштабирование данных
scaler = StandardScaler()
X_train_poly_scaled = scaler.fit_transform(X_train_poly)
X_test_poly_scaled = scaler.transform(X_test_poly)

# Создание и обучение модели регрессии Риджа
ridge_model = Ridge(alpha=0.1)  # Установка параметра регуляризации
ridge_model.fit(X_train_poly_scaled, y_train)

# Предсказание на тестовых данных
y_pred_ridge_poly = ridge_model.predict(X_test_poly_scaled)

# Вычисление R^2
r2_ridge_poly = r2_score(y_test, y_pred_ridge_poly)
print(f"Коэффициент детерминации (R²) для полиномиальной регрессии Риджа: {r2_ridge_poly:.4f}")
