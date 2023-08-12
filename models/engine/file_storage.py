#!/usr/bin/python3
"""
contains class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets obj with the key <obj class name>.id in the __obj dictionary
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            my_dict = {
                    index: self.__objects[index].to_dict()
                    for index in self.__objects.keys()
            }
            json.dump(my_dict, file)

    def reload(self):
        """
        deserialize json file to __object
        does nothing if the file or filepath does not exist
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                my_dict = json.load(file)
                for dict_obj in my_dict.values():
                    clsname = dict_obj["__class__"]
                    del dict_obj["__class__"]
                    self.new(eval(clsname)(**dict_obj))
        except FileNotFoundError:
            pass
