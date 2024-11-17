#!/usr/bin/python3
"""Defines the FileStorage class"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object"""
        key = (f"{__class__.__name__}.{obj.id}")
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({
                        k: v.to_dict()
                        for k, v in self.__objects.items()
                    }, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists"""
        try:
           with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    # Assume that the classes have already
                    # been defined and imported
                    cls_name = value["__class__"]
                    cls = globals()[cls_name]
                    # or import your specific classes
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
