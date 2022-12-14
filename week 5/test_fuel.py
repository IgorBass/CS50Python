from fuel import convert
from fuel import gauge
import pytest

def test_34():
    assert convert('3/4') == 75

def test_13():
    assert convert('1/3') == 33

def test_23():
    assert convert('2/3') == 67

def test_0():
    assert convert('0/100') == 0

def test_100():
    assert convert('100/100') == 100

def test_100F():
    assert gauge(100) == 'F'

def test_0e():
    assert gauge(0) == 'E'

def test_1e():
    assert gauge(1) == 'E'

def test_99F():
    assert gauge(99) == 'F'

def test_50prcnt():
    assert gauge(50) == '50%'

def test_str():
    with pytest.raises(ValueError):
        convert('four/five')

def test_fms():
    with pytest.raises(ValueError):
        convert('100/1')

def test_divZero():
    with pytest.raises(ZeroDivisionError):
        convert('50/0')