import unittest
from io import BytesIO
import pandas as pd
from unittest.mock import Mock, patch
from predictions.services.prediction_service import (
    validate_file_extension,
    load_excel_file,
    validate_columns,
    load_model,
    make_predictions,
)

class TestUtilityFunctions(unittest.TestCase):

    def test_validate_file_extension_valid(self):
        validate_file_extension("archivo.xlsx")  

    def test_validate_file_extension_invalid(self):
        with self.assertRaises(ValueError) as context:
            validate_file_extension("archivo.txt")
        self.assertIn("Por favor, cargue un archivo Excel válido con extensión .xlsx.", str(context.exception))

    def test_load_excel_file_valid(self):
        # Crear un archivo Excel de prueba
        excel_data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        excel_bytes = BytesIO()
        excel_data.to_excel(excel_bytes, index=False)
        excel_bytes.seek(0)

        # Cargar el archivo con la función
        loaded_data = load_excel_file(excel_bytes)
        pd.testing.assert_frame_equal(loaded_data, excel_data)

    def test_load_excel_file_invalid(self):
        invalid_file = BytesIO(b"not a valid Excel file")
        with self.assertRaises(ValueError) as context:
            load_excel_file(invalid_file)
        self.assertIn("Error al leer el archivo Excel", str(context.exception))

    def test_validate_columns_valid(self):
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        validate_columns(data, ["col1", "col2"])  

    def test_validate_columns_invalid(self):
        data = pd.DataFrame({"col1": [1, 2]})
        with self.assertRaises(ValueError) as context:
            validate_columns(data, ["col1", "col2"])
        self.assertIn("El archivo no contiene las columnas necesarias: col1, col2", str(context.exception))

    @patch("joblib.load")
    def test_load_model_valid(self, mock_joblib_load):
        mock_joblib_load.return_value = "mock_model"
        model = load_model("dummy_path")
        self.assertEqual(model, "mock_model")

    @patch("joblib.load")
    def test_load_model_file_not_found(self, mock_joblib_load):
        mock_joblib_load.side_effect = FileNotFoundError()
        with self.assertRaises(FileNotFoundError) as context:
            load_model("dummy_path")
        self.assertIn("El archivo del modelo no se encontró", str(context.exception))

    @patch("joblib.load")
    def test_load_model_generic_error(self, mock_joblib_load):
        mock_joblib_load.side_effect = Exception("mock error")
        with self.assertRaises(Exception) as context:
            load_model("dummy_path")
        self.assertIn("Error al cargar el modelo: mock error", str(context.exception))

    def test_make_predictions_valid(self):
        mock_model = Mock()
        mock_model.predict.return_value = [0, 1]
        predictions = make_predictions(mock_model, [[1, 2], [3, 4]])
        self.assertEqual(predictions, [0, 1])

    def test_make_predictions_value_error(self):
        mock_model = Mock()
        mock_model.predict.side_effect = ValueError("mock prediction error")
        with self.assertRaises(ValueError) as context:
            make_predictions(mock_model, [[1, 2]])
        self.assertIn("Error en las predicciones: mock prediction error", str(context.exception))

    def test_make_predictions_generic_error(self):
        mock_model = Mock()
        mock_model.predict.side_effect = Exception("unexpected error")
        with self.assertRaises(Exception) as context:
            make_predictions(mock_model, [[1, 2]])
        self.assertIn("Error inesperado al realizar las predicciones: unexpected error", str(context.exception))

if __name__ == "__main__":
    unittest.main()
