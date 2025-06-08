from unittest.mock import patch, mock_open
from src.utils import operations_list

@patch("builtins.open", new_callable=mock_open, read_data='{"id": "1"}')
def test_operations_list(mock_file, operation_str):
    operation_str = operations_list("test.json")
    assert operation_str == {"id": "1"}
