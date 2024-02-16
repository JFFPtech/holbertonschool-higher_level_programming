import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        """Test Square initialization"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3, 1)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 1)
    
    def test_str(self):
        """Test Square __str__ method"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(10, 2, 3, 1)
        self.assertEqual(str(s2), "[Square] (1) 2/3 - 10")

    def test_size(self):
        """Test Square size property"""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

    def test_update(self):
        """Test Square update method"""
        s1 = Square(5)
        s1.update(1, 10, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

        s2 = Square(5)
        s2.update(id=2, size=8, x=4, y=5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 8)
        self.assertEqual(s2.x, 4)
        self.assertEqual(s2.y, 5)

    def test_to_dictionary(self):
        """Test Square to_dictionary method"""
        s1 = Square(5, 2, 3, 1)
        dictionary = s1.to_dictionary()
        self.assertEqual(dictionary, {"id": 1, "size": 5, "x": 2, "y": 3})

if __name__ == '__main__':
    unittest.main()