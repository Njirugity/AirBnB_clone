#!/usr/bin/python3

"""Defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the class City that inherits from BaseModel"""
    state_id: str = ""
    name: str = ""
