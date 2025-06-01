import pytest


from src.decorators import log


def test_log_error(capsys):
    @log()
    def func_test(a, b):
        raise ValueError('test error')

    try:
        func_test(1, 2)
    except ValueError:
        pass

    captured = capsys.readouterr()
    assert 'func_test error: ValueError. Inputs: (1, 2), {}\n' in captured.out


def test_log():
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3
