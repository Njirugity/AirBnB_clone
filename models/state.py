#!/usr/bin/python3

"""Defines the class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the class state that inherits from BaseModel"""
    name: str = ""
