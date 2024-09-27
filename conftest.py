import pytest


@pytest.fixture(scope='session')
def myfixture():
    print("Myfixture is called")
    yield
    print("last code is executed")


@pytest.fixture()
def userprofile():
    print("User prfile is being creted")
    return ["chetan", "Sukku"]


@pytest.fixture(params=[("chrome", "chetan", "Netekal"),("firefox", "sukku", "chinnu"),("IE", "Sunil", "shetty")])
def dataLoad(request):
    print("crossBrowser is being called")
    return request.param
