from numb3rs import validate
import pytest

def test_answer_1():
    assert validate('127.0.0.1')

def test_answer_2():
    assert validate('255.255.255.255')

def test_answer_3():
    assert validate('140.247.235.144')

def test_answer_4():
    assert not validate('256.255.255.255')

def test_answer_5():
    assert not validate('64.128.256.512')

def test_answer_6():
    assert not validate('2001:09db:85a3:0000:0000:8a2e:0370:7334')

def test_answer_7():
    assert not validate('cat')

def test_answer_8():
    assert not validate('123')
