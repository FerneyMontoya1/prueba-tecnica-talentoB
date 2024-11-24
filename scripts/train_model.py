from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Carga los datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Entrena un modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guarda el modelo en un archivo
joblib.dump(model, "iris_model.pkl")

print("Modelo entrenado y guardado como iris_model.pkl")
