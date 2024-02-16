import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_base__init__(self):
        """Test Base initialization"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """Test Base to_json_string method"""
        b1 = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_save_to_file(self):
        """Test Base save_to_file method"""
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """Test Base from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_create(self):
        """Test Base create method"""
        r1 = Rectangle(3, 5, 1, 2, 10)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(str(r2), "[Rectangle] (10) 1/2 - 3/5")

    def test_load_from_file(self):
        """Test Base load_from_file method"""
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

if __name__ == '__main__':
    unittest.main()