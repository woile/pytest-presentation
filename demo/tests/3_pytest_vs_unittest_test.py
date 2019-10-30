import pytest
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper_yes(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        print("what's going on?")
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_lower_yes(self):
        print("what's going on?")
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    @pytest.mark.awesome
    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
