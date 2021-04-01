#this is an example

temperature = 10

def print_temperature():
    print(temperature)

def add(a,b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def substract(a, b):
    return a + b

def test_substract():
    assert substract(2, 3) == -1
