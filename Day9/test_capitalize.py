import pytest
from main import capital_case

# print(pytest)
# these are all the test functions 

def test_capital_case():
    assert capital_case('party') == 'Party'
    assert capital_case('ALL CAPS') == 'All caps'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)