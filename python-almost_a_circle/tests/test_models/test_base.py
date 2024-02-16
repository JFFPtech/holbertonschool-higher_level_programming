import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_base(self):
        """Test base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base()
        self.assertEqual(b5.id, 4)
    
    def test_create(self, **dictionary):
        """Test create method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)
        s1 = Square(5, 3, 1)
        dictionary = s1.to_dictionary()
        s2 = Square.create(**dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertFalse(s1 is s2)
    
    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "size": 10, "y": 2, "x": 7}, {"id": 2, "size": 2, "y": 0, "x": 0}]')
