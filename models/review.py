#!/usr/bin/python3

"""Defines the class Review"""
from model.base_model import BaseModel


class Review(BaseModel):
    """ Represents the class Review that inherits from BaseModel"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
