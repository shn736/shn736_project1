import unittest
from unittest.mock import mock_open, patch
from src.reading_operations import reading_operations_excel, reading_operations_csv


class TestReadingOperationsCSV(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="date,amount\n2023-01-01,100\n2023-01-02,200")
    def test_reading_operations_success(self, mock_file):
        expected = [{'amount': '100', 'date': '2023-01-01'}]
        result = reading_operations_csv("dummy_path.csv")
        self.assertEqual(result, expected)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        result = reading_operations_csv("dummy_path.csv")
        self.assertEqual(result, "Ошибка: Файл по пути 'dummy_path.csv' не найден.")

    @patch("builtins.open", side_effect=Exception("Неизвестная ошибка"))
    def test_general_error(self, mock_file):
        result = reading_operations_csv("dummy_path.csv")
        self.assertEqual(result, "Произошла ошибка: Неизвестная ошибка")


class TestReadingOperationsExcel(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_file_not_found(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError

        result = reading_operations_excel("invalid_path.xlsx")

        # Проверка сообщения об ошибке
        self.assertEqual(result, "Ошибка: Файл не найден по указанному пути: invalid_path.xlsx")

    @patch('pandas.read_excel')
    def test_value_error(self, mock_read_excel):
        mock_read_excel.side_effect = ValueError

        result = reading_operations_excel("other_path.xlsx")

        # Проверка сообщения об ошибке
        self.assertEqual(result, "Ошибка: Не удалось прочитать файл. Убедитесь, что это файл Excel.")

    @patch('pandas.read_excel')
    def test_generic_exception(self, mock_read_excel):
        mock_read_excel.side_effect = Exception("Some error")

        result = reading_operations_excel("some_path.xlsx")

        # Проверка сообщения об ошибке
        self.assertEqual(result, "Произошла ошибка: Some error")
