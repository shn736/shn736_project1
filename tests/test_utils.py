from unittest.mock import patch, mock_open
from src.utils import operations_list
import unittest


class TestOperationsList(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "action": "test"}]')
    def test_operations_list_valid_json(self, mock_file):
        result = operations_list('dummy_path')
        expected = [{"id": 1, "action": "test"}]
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data='invalid json')
    def test_operations_list_invalid_json(self, mock_file):
        result = operations_list('dummy_path')
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_operations_list_file_not_found(self, mock_file):
        result = operations_list('dummy_path')
        self.assertEqual(result, [])
