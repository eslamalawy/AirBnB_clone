#!/usr/bin/python3
"""contains User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class based off BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
