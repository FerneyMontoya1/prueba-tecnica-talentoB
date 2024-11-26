from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Carga los datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Entrena un modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evalúa el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Guarda el modelo y la precisión
joblib.dump((model, accuracy), "iris_model.pkl")
print(f"Modelo entrenado y guardado como iris_model.pkl con precisión: {accuracy:.2f}")
