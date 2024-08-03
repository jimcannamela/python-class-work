from user_input import get_valid_us_state
from user_input import get_valid_temp_measurement
from unittest.mock import patch

#########################################     get_valid_us_state()     #########################################
def test_get_valid_us_state_by_state_code_upper():
    with patch('builtins.input', side_effect=['AZZ', 'another_invalid', 'AZ']):
        result = get_valid_us_state()
        assert result == 'AZ'

def test_get_valid_us_state_by_state_code_lower():
    with patch('builtins.input', side_effect=['AZZ', 'another_invalid', 'az']):
        result = get_valid_us_state()
        assert result == 'AZ'

def test_get_valid_us_state_by_state_name():
    with patch('builtins.input', side_effect=['AZZ', 'another_invalid', 'arizona']):
        result = get_valid_us_state()
        assert result == 'AZ'

#########################################     test_get_valid_temp_measurement()     #########################################
def test_get_valid_temp_measurement_F():
    with patch('builtins.input', side_effect=['FF', 'CC', 'F']):
        result = get_valid_temp_measurement()
        assert result == 'imperial'

def test_get_valid_temp_measurement_C():
    with patch('builtins.input', side_effect=['2379827', '', 'C']):
        result = get_valid_temp_measurement()
        assert result == 'metric'