import pandas as pd
import joblib
from django.shortcuts import render
from django.http import HttpResponse

def upload_and_predict(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        try:
            # Verifica si el archivo tiene la extensión correcta
            if not excel_file.name.endswith(".xlsx"):
                return HttpResponse("Por favor, cargue un archivo Excel válido con extensión .xlsx.", status=400)

            # Intenta leer el archivo Excel
            try:
                data = pd.read_excel(excel_file)
            except Exception as e:
                return HttpResponse(f"Error al leer el archivo Excel: {str(e)}", status=400)

            # Verifica si las columnas necesarias están presentes
            required_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
            if not all(col in data.columns for col in required_columns):
                return HttpResponse("El archivo no contiene las columnas necesarias: sepal_length, sepal_width, petal_length, petal_width", status=400)

            # Carga el modelo entrenado
            try:
                model = joblib.load("predictions/model/iris_model.pkl")
            except FileNotFoundError:
                return HttpResponse("El archivo del modelo no se encontró. Verifica la ruta y vuelve a intentarlo.", status=500)
            except Exception as e:
                return HttpResponse(f"Error al cargar el modelo: {str(e)}", status=500)

            # Realiza las predicciones con las características numéricas
            try:
                features = data[required_columns]
                predictions = model.predict(features)
            except ValueError as ve:
                return HttpResponse(f"Error en las predicciones: {str(ve)}. Verifique los datos del archivo.", status=400)
            except Exception as e:
                return HttpResponse(f"Error inesperado al realizar las predicciones: {str(e)}", status=500)

            # Agrega las predicciones al DataFrame
            data["Predictions"] = predictions

            # Envía los resultados a la plantilla
            return render(request, "predictions/results.html", {"table": data.to_html()})

        except Exception as e:
            return HttpResponse(f"Error inesperado: {str(e)}", status=500)

    # Renderiza la página de subida en caso de solicitud GET o ausencia del archivo
    return render(request, "predictions/upload.html")
