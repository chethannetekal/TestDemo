
import pytest

@pytest.mark.usefixtures("myfixture")
class Test2:

    def test_method4(self):
        print("Method4 is called")

    def test_method5(self):
        print("Method5 is called")

