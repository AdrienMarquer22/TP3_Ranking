import unittest
import re
from ranking.utils import token_clean


class TestTokenClean(unittest.TestCase):
    def test_token_clean(self):
        self.assertEqual(token_clean("Hello World!"), ["hello", "world"])
        self.assertEqual(token_clean("Testing, 1-2-3..."), ["testing", "123"])
        self.assertEqual(token_clean("One Two Three"), ["one", "two", "three"])
