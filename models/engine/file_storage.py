#!/usr/bin/python3
"""
contains class FileStorage
"""
import json, os

class FileStorage:
    """
    class that serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "models/engine/file.json"
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
        self.__objects[f"{obj.__class__.__name__}.id"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        deserialize json file to __object
        does nothing if the file or filepath does not exist
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        else:
            pass



