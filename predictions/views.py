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
    table = None  # Inicializa la tabla como `None`
    error_message = None  # Variable para manejar errores

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

            # Convertir la tabla en HTML
            table = data.to_html(
                classes="table table-bordered table-striped", index=False, justify="center"
            )

        except ValueError as ve:
            error_message = str(ve)
        except FileNotFoundError as fnfe:
            error_message = str(fnfe)
        except Exception as e:
            error_message = f"Error inesperado: {str(e)}"

    # Renderizar el formulario y, si existe, la tabla
    return render(request, "predictions/upload.html", {"table": table, "error_message": error_message})
