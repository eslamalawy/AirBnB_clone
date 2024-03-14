#!/bin/usr/python3
"""file containing basemodel class"""
from datetime import datetime
from models import storage
import uuid


class BaseModel():
    """Class BaseModel, base model for AirBnB Clone"""

    def __init__(self, *args, **kwargs):
        """initializes BaseModel"""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """class str method"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary of BaseModel"""
        self_dictionary = dict(self.__dict__)
        self_dictionary['__class__'] = self.__class__.__name__
        self_dictionary['created_at'] = datetime.isoformat(self.created_at)
        self_dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return self_dictionary
