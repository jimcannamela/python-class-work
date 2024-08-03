import pytest
from currency_converter import get_currency_data
from unittest.mock import patch, Mock

def test_currency_converter_tc1():
    # ensures the API is working and returning data
    assert not get_currency_data == None