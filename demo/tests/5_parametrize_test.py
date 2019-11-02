import pytest


def generate_version(current_version, increment):
    pass


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("2.0.0", "PATCH"), "2.0.1"),
        (("2.0.1", "PATCH"), "2.0.2"),
        (("2.0.2", "MINOR"), "2.1.0"),
        (("2.1.0", "MAJOR"), "3.0.0"),
    ],
)
def test_generate_version(test_input, expected):
    assert generate_version(test_input[0], test_input[1]) == expected
