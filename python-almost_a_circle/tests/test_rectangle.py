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
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            r.display()
            self.assertEqual(fakeOutput.getvalue(), expected_output)
        r = Rectangle(2, 3, 2, 1)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            r.display()
            self.assertEqual(fakeOutput.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        """Test update method"""
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(2, 7, 12, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(width=8, height=15, x=6, y=7)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        self.assertEqual(r.to_dictionary(), expected_output)

if __name__ == "__main__":
    unittest.main()