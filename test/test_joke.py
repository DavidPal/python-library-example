import unittest

from joke import joke


class TestJoke(unittest.TestCase):

    def test(self):
        # Check that the joke has at least 5 characters.
        self.assertTrue(len(joke.tell_joke()) >= 5)


if __name__ == "__main__":
    unittest.main()
