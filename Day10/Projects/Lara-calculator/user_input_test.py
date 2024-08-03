from unittest.mock import patch
import user_input
import operator
import pytest

def test_get_float_input_valid_input():
    with patch('builtins.input', side_effect=['5']):
        result = user_input.get_float_input()
        assert result == 5

def test_get_float_input_invalid_input():
    with patch('builtins.input', side_effect=['invalid', 'another_invalid', '3.14']):
        result = user_input.get_float_input()
        assert result == 3.14

def test_get_operator_input_only_valid_input_add():
    with patch('builtins.input', side_effect=['+']):
        result = user_input.get_operator_input()
        assert result == operator.add

def test_get_operator_input_only_valid_input_div():
    with patch('builtins.input', side_effect=['-']):
        result = user_input.get_operator_input()
        assert result == operator.sub

def test_get_operator_input_only_valid_input_mul():
    with patch('builtins.input', side_effect=['*']):
        result = user_input.get_operator_input()
        assert result == operator.mul

def test_get_operator_input_only_valid_input_div():
    with patch('builtins.input', side_effect=['/']):
        result = user_input.get_operator_input()
        assert result == operator.truediv

def test_get_operator_input_only_valid_input_pow():
    with patch('builtins.input', side_effect=['^']):
        result = user_input.get_operator_input()
        assert result == operator.pow

def test_get_operator_input_only_valid_input_mod():
    with patch('builtins.input', side_effect=['%']):
        result = user_input.get_operator_input()
        assert result == operator.mod

def test_get_operator_input_invalid_input():
    with patch('builtins.input', side_effect=['++', '+']):
        result = user_input.get_operator_input()
        assert result == operator.add

def test_get_operator_input_only_invalid_input():
    with pytest.raises(StopIteration):
        with patch('builtins.input', side_effect=['++']):
            user_input.get_operator_input()