import pandas as pd
import joblib
from django.shortcuts import render
from django.http import HttpResponse

def upload_and_predict(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        # Lee el archivo Excel
        data = pd.read_excel(excel_file)

        print("Columnas en el archivo Excel:", data.columns)

        # Verifica si las columnas necesarias están presentes
        required_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        if not all(col in data.columns for col in required_columns):
            return HttpResponse("El archivo no contiene las columnas necesarias.", status=400)

        # Carga el modelo entrenado
        model = joblib.load("predictions/model/iris_model.pkl")
        print("Modelo cargado exitosamente")

        # Elimina la columna 'species' antes de pasar las características al modelo
        features = data[required_columns]

        # Realiza las predicciones con las características numéricas
        predictions = model.predict(features)

        # Agrega las predicciones al DataFrame
        data["Predictions"] = predictions

        # Envía los resultados a la plantilla
        return render(request, "predictions/results.html", {"table": data.to_html()})

    return render(request, "predictions/upload.html")
