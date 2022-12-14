from blueprints.generic.views import hello_world


def test_hello_world_lower():
    hello_string = hello_world()
    assert hello_string.lower() == "hello world"


def test_hello_world_pass():
    hello_string = hello_world()
    assert hello_string == "Hello World"

def test_pass():
    condition = True
    assert condition is False
