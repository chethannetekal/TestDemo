import pytest


class TestDepends:
    @pytest.mark.dependency()
    def test_method11(self):
        print("method-11 is called")
        assert 2+3 == 5

    @pytest.mark.dependency(depends=["TestDepends::test_method11"])
    def test_method12(self):
        print("method-12 is called")

    def test_method13(self):
        print("method-13 is called")


class TestDepends1:
    @pytest.mark.dependency(depends= ["TestDepends::test_method11"])
    def test_method14(self):
        print("method-14 is called")



