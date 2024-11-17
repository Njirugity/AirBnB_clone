#!/usr/bin/python3

""" Test BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Represents unit test for BaseModel"""
    def test_init(self):
        """Test initialization of attributes"""
        myModel = BaseModel()
        self.assertIsNotNone(myModel.id)
        self.assertIsNotNone(myModel.created_at)
        self.assertIsNotNone(myModel.updated_at)

    def test_save(self):
        """Test save() method for update_at"""
        myModel = BaseModel()
        initial = myModel.updated_at
        current = myModel.save()
        self.assertNotEqual(initial, current)

    def test_to_dict(self):
        """Test type of to_dict() method"""
        myModel = BaseModel()
        myModel_dict = myModel.to_dict()
        self.assertIsInstance(myModel_dict, dict)
        self.assertEqual(myModel_dict["__class__"], "BaseModel")
        self.assertEqual(myModel_dict["id"], myModel.id)
        self.assertEqual(
            myModel_dict["created_at"], myModel.created_at.isoformat()
            )
        self.assertEqual(
            myModel_dict["updated_at"], myModel.updated_at.isoformat()
            )

    def test_str(self):
        """Test string representation"""
        myModel = BaseModel()
        self.assertTrue(str(myModel).startswith("[BaseModel]"))
        self.assertIn(myModel.id, str(myModel))
        self.assertIn(str(myModel.__dict__), str(myModel))


if __name__ == "__main__":
    unittest.main()
