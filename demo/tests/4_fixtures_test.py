import pytest
import os
import tempfile


# @pytest.fixture(scope="module")
@pytest.fixture()
def get_customer():
    return {"name": "jon"}


def test_customer_name(get_customer):
    print(hex(id(get_customer)))
    assert get_customer["name"] == "jon"


def test_customer_name2(get_customer):
    print(hex(id(get_customer)))
    assert get_customer["name"] != "mike"


@pytest.fixture()
def temp_file():
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, "w") as tmp:
        # do stuff with temp file
        tmp.write("stuff")
    yield path
    os.remove(path)


def test_istmp(temp_file):
    assert "tmp" in temp_file


@pytest.fixture()
def new_customer():
    def _new_customer(name):
        return {"name": name}

    return _new_customer


def test_multi_customers(new_customer):
    customer_1 = new_customer("jon")
    customer_2 = new_customer("mike")

    assert customer_1["name"] == "jon"
    assert customer_2["name"] == "mike"
