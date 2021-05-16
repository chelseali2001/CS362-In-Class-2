import pytest
import palindrome

def test_true():
    assert palindrome.palin("radar") == True

def test_trueCap():
    assert palindrome.palin("radAr") == True

def test_false():
    assert palindrome.palin("Chelsea") == False

def test_type():
    assert palindrome.palin(9) == True