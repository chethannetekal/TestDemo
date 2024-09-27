#How to call fixture from a test method:
import pytest


class Test4:
    @pytest.fixture(scope='class')
    def myfixture2(self):
        print("myfixture2 is called")

    def test_method8(self, myfixture2):
        print("method8 is called")
        print(myfixture2)

    def test_method9(self, myfixture2):
        print("method9 is called")
        print(myfixture2)