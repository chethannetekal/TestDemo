#How to run a specific method before each test method in a class using fixture
import pytest


@pytest.mark.usefixtures("myfixture")
class Test:

    def test_method1(self):
        print("Method1 is called")

    def test_method2(self):
        print("Method2 is called")

    def test_method3(self):
        print("Method3 is called")