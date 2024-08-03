import pytest
from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome('madam')

def test_is_palindrome_with_capitol_letters():
    assert is_palindrome('Madam')

def test_is_palindrome_with_spaces():
    assert is_palindrome('never odd or even')

def test_is_palindrome_with_special_characters():
    assert is_palindrome("A toyota's a toyota")

def test_is_not_a_palindrome():
    assert not is_palindrome('abcedf')

def test_is_not_a_palindrome_with_spaces():
    assert not is_palindrome('Four score and seven years ago')


# Brad's tests
# def test_is_palindrome():
#     assert is_palindrome("racecar") == True
#     assert is_palindrome("NeVeR oDd Or EvEn") == True
#     assert is_palindrome("A man, a plan, a canal, Panama!")
#     assert is_palindrome("Banana") == False
#     assert is_palindrome("Hello World") == False
#     assert is_palindrome("") == True
#     assert is_palindrome("894537./,") == True
#     assert is_palindrome("a894537./,b") == False
#     assert is_palindrome("a894537./,A") == True