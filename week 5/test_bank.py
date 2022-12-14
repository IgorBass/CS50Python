from bank import value

def test_hello():
    assert value('hello') == 0

def test_Hello():
    assert value('Hello') == 0

def test_with_name():
    assert value('Hello,Igor') == 0

def test_HYD():
    assert value('How you doing?') == 20

def test_whatsup():
    assert value("What'sup?") == 100

def test_WH():
    assert value("Whatishappening") == 100