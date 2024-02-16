import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test initialization"""
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_width(self):
        """Test width property"""
        r = Rectangle(5, 10)
        r.width = 7
        self.assertEqual(r.width, 7)
        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height(self):
        """Test height property"""
        r = Rectangle(5, 10)
        r.height = 12
        self.assertEqual(r.height, 12)
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(ValueError):
            r.height = -8

    def test_x(self):
        """Test x property"""
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -2

    def test_y(self):
        """Test y property"""
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """Test area method"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test display method"""
        r = Rectangle(3, 2)
        self.assertEqual(r.display(), None)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Test update method"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        self.assertEqual(r.to_dictionary(), expected_output)

if __name__ == "__main__":
    unittest.main()