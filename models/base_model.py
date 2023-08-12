#!/usr/bin/python3
"""
This contains BaseModel class from which other classes will inherit
"""
import uuid
import datetime
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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    elif key == "updated_at":
                        self.updated_at = datetime.datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
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
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["id"] = self.id
        return self.__dict__
