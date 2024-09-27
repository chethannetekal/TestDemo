import pytest


class Test3:

    @pytest.fixture(scope='class')
    def myfixture2(self, request):
        print("my fixture is called")

        def teardown():
            print("teardown is called")
        request.addfinalizer(teardown)

    def test_method6(self):
        print("Method6 is called")

    def test_method7(self):
        print("Method7 is called")
