#!/usr/bin/python3
""" Defines the class File Strorage for serializing and deserializing"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """Represent the FileStorage class"""
    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns the dictionary __object"""
        return FileStorage.__object

    def new(self, obj):
        """Stores a new object"""
        key = (f"{__class__.__name__}.{obj.id}")
        FileStorage.__object[key] = obj

    def save(self):
        """Serialize an object to a JSON file"""
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__object.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dumps(obj_dict, f)

    def reload(self):
        """ Deserialize a JSON file"""
        try:
            obj_deserialized = {}
            with open(FileStorage, "r") as f:
                obj_deserialized = json.loads(f.read())
            FileStorage.__objects = {
                key: eval(val["__class__"])(**val)
                for key, val in obj_deserialized.items()
            }
        except Exception:
            pass
