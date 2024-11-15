#!/usr/bin/python3
# models/engine/file_storage.py
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    # Assume that the classes have already been defined and imported
                    cls_name = value["__class__"]
                    cls = globals()[cls_name]  # or import your specific classes
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

