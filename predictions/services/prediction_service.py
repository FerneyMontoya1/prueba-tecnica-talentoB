import pandas as pd
import joblib

def validate_file_extension(file_name):
    if not file_name.endswith(".xlsx"):
        raise ValueError("Por favor, cargue un archivo Excel válido con extensión .xlsx.")

def load_excel_file(file):
    try:
        return pd.read_excel(file)
    except Exception as e:
        raise ValueError(f"Error al leer el archivo Excel: {str(e)}")

def validate_columns(data, required_columns):
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"El archivo no contiene las columnas necesarias: {', '.join(required_columns)}")

def load_model(model_path):
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo del modelo no se encontró. Verifica la ruta y vuelve a intentarlo.")
    except Exception as e:
        raise Exception(f"Error al cargar el modelo: {str(e)}")

def make_predictions(model, features):
    try:
        return model.predict(features)
    except ValueError as ve:
        raise ValueError(f"Error en las predicciones: {str(ve)}")
    except Exception as e:
        raise Exception(f"Error inesperado al realizar las predicciones: {str(e)}")
