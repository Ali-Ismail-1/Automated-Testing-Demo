from blueprints.generic.views import hello_world

def test_hello_world():
    hello_string = hello_world()
    assert hello_world == "hello world"
