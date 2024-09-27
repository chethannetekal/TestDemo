import pytest


@pytest.mark.usefixtures()
def test_method9(userprofile):
    print(userprofile)


@pytest.mark.usefixtures
def test_method(dataLoad):
    print(dataLoad)
