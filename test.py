from helloworld import say_hello

def test_helloworld_no_params():
    assert say_hello() == 'Hello, World!'


def test_helloworld_with_params():
    assert say_hello('Everybody') == 'Hello, Everyone!'