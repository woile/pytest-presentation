import unittest


class TestStringMethods(unittest.TestCase):
    def get_location(self) -> str:
        return "amsterdam"

    def test_location(self):
        assert self.get_location() == "bordeaux"
        # assert get_location() == "amsterdam"
