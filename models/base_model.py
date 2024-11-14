#!/usr/bin/python3

"""Defines the class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """The parent class for other classes. Describes the BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
    	    for key, value in kwargs.items():
                if key == __class__:
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], date_format)
                else:
                    self.id = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of instance attributes"""
        temp = self.__dict__.copy()
        temp["__class__"] = self.__class__.__name__
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        return temp

    def __str__(self):
        """Returns a string representation"""
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) ({self.__dict__})")
