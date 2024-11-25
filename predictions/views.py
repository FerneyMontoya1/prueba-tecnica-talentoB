from django.shortcuts import render
from django.http import HttpResponse
from .services.prediction_service import (
    validate_file_extension,
    load_excel_file,
    validate_columns,
    load_model,
    make_predictions,
)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_and_predict(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        try:
            # Validación de la extensión del archivo
            validate_file_extension(excel_file.name)

            # Cargar el archivo Excel
            data = load_excel_file(excel_file)

            # Validar columnas necesarias
            required_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
            validate_columns(data, required_columns)

            # Cargar el modelo
            model_path = "predictions/model/iris_model.pkl"
            model = load_model(model_path)

            # Realizar predicciones
            features = data[required_columns]
            predictions = make_predictions(model, features)

            # Agregar predicciones al DataFrame
            data["Predictions"] = predictions

            # Renderizar los resultados
            return render(request, "predictions/results.html", {"table": data.to_html()})

        except ValueError as ve:
            return HttpResponse(str(ve), status=400)
        except FileNotFoundError as fnfe:
            return HttpResponse(str(fnfe), status=500)
        except Exception as e:
            return HttpResponse(f"Error inesperado: {str(e)}", status=500)

    return render(request, "predictions/upload.html")
