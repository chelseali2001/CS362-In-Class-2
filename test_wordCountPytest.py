import pytest
import wordCount

def test_pass():
    assert wordCount.count("CS362") == 1

def test_passMulti():
    assert wordCount.count("This is an activity") == 4

def test_type():
    assert wordCount.count(32) == 1