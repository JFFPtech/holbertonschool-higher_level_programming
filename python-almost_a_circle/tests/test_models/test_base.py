#!/usr/bin/python3
"""Unittest for base.py
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for base class
    """

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def test_init_with_id(self):
        """Test __init__ method with id parameter"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_init_without_id(self):
        """Test __init__ method without id parameter"""
        b = Base()
        self.assertEqual(b.id, 1)


if __name__ == '__main__':
    unittest.main()