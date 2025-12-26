import os

from mock_lib import greet

def test_greet_name():
    assert greet("Arres") == "Hello, Arres!"

def test_greet_default():
    assert greet("") == "Hello, world!"
