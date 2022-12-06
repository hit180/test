from add_num import add
import pytest

import unittest

class TestStringMethods(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(add(2,2), 4)

if __name__ == '__main__':
    unittest.main()

