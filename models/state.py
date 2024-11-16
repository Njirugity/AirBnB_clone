#!/usr/bin/python3

"""Defines the class State"""
from models.basemodel import BaseModel


class State(BaseModel):
    """Represents the class state that inherits from BaseModel"""
    name: str = ""
