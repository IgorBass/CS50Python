from twttr import shorten

def test_numbers():
    assert shorten('1234567890') == '1234567890'

def test_word():
    assert shorten('Twitter') == 'Twttr'

def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_alnum():
    assert shorten('CS50') == 'CS50'

def test_upppercase():
    assert shorten('PYTHON') == 'PYTHN'