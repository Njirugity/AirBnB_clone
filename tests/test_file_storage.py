#!/usr/bin/python3
"""Test FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """Represents testcases for FileStorage class"""

    def test_FileStorageInstantationWithout(self):
        """Test creating FileStorage instance with no arg"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorageInstantationWith(self):
        """Test creating FileStorage instance with arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def setUp(self):
        """Creates a temporary test file"""
        self.test_file = "test_file.json"

    def test_all(self):
        """Test if the all() method returns dict"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new_with_args(self):
        """Test creating a new object with extra args
        :Should raise TypeError"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 2)

    def test_new_None(self):
        """Test creating a new object with None
        :Should raise TypeError"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)


if __name__ == "__main__":
    unittest.main()
