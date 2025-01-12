from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

# Масштабирование данных
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Создание и обучение модели регрессии Риджа
ridge_model = Ridge(alpha=0.1)  # Установка параметра регуляризации
ridge_model.fit(X_train_scaled, y_train)

# Предсказание на тестовых данных
y_pred_ridge = ridge_model.predict(X_test_scaled)

# Вычисление R^2
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"Коэффициент детерминации (R²) для регрессии Риджа: {r2_ridge:.4f}")
