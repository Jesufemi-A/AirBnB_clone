#!/usr/bin/python3
"""
This contains BaseModel class from which other classes will inherit
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        initialises the instance attributes everytime an object
        is created

        args:
        self - refers to the instance itself
        """
        date_f = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.strptime(value, date_f)
                    elif key == "updated_at":
                        i self.updated_at = datetime.strptime(value, date_f)
                    else:
                        setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """
        returns a human readeable representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        base_dict["id"] = self.id
        return base_dict
