#!/usr/bin/python3
"""
Contains class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    inherit from BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
