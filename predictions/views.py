from django.shortcuts import render
from django.http import HttpResponse
from .services.prediction_service import (
    validate_file_extension,
    load_excel_file,
    validate_columns,
    load_model,
    make_predictions,
    generate_statistics,  
)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_and_predict(request):
    table = None
    error_message = None
    stats = None

    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        try:
            validate_file_extension(excel_file.name)
            data = load_excel_file(excel_file)

            required_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
            validate_columns(data, required_columns)

            model_path = "predictions/model/iris_model.pkl"
            model = load_model(model_path)

            features = data[required_columns]
            predictions = make_predictions(model, features)

            # Calcular precisión solo si existe "actual"
            accuracy = None
            if "actual" in data.columns:
                accuracy = (predictions == data["actual"]).mean()

            stats = generate_statistics(predictions, accuracy)

            data["Predictions"] = predictions
            table = data.to_html(classes="table table-bordered table-striped", index=False, justify="center")

        except ValueError as ve:
            error_message = str(ve)
        except FileNotFoundError as fnfe:
            error_message = str(fnfe)
        except Exception as e:
            error_message = f"Error inesperado: {str(e)}"

    return render(request, "predictions/upload.html", {"table": table, "error_message": error_message, "stats": stats})
