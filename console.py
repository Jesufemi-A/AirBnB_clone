#!/usr/bin/python3
"""
contains class HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models.base_model import models
import re


class HBNBCommand(cmd.Cmd):
    """
    class to create command line interpreter
    """
    prompt = "(hbnb) "
    classnames = ["BaseModel",
                "User", "Place", "City",
                    "State", "Amenity", "Review"]

    def do_quit(self, line):
        """
        Quit the commandline interpreter
        """
        exit()

    def do_EOF(self, line):
        """
        Method that handles the End-of_file
        """
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the
        command prompt
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        split = line.split(" ")
        if len(split) == 1 and split[0] == "":
            print("** class name is missing **")
        elif len(split) == 1 and split[0] not in self.classnames:
            print("** class doesn't exist **")
        instance = eval(split[0])()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        split = line.split(" ")
        if len(split) == 1 and split[0] == "":
            print("** class name is missing **")
        elif len(split) == 1 and split[0] not in self.classnames:
            print("** class doesn't exist **")
        elif len(split) == 1:
            print("** instance id missing **")
        elif f"{split[0]}.{split[1]}" not in models.storage.all().keys():
            print("** no instance found **")
        else:
            instance = models.storage.all()[f"{split[0]}.{split[1]}"]
            print(instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file)
        """
        split = line.split(" ")
        if len(split) == 1 and split[0] == "":
            print("** class name missing **")
        elif len(split) == 1 and split[0] not in self.classnames:
            print("** class doesn't exist **")
        elif len(split) == 1 and split[0] in self.classnames:
            print("** instance id missing **")
        elif len(split) == 2 and split[1] in self.classnames:
            instance = models.storage.all()[f"{split[0]}.{split[1]}"]
            if not instance:
                print("** no instance found **")
            else:
                del instance
                models.storage.all().save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        split = line.split(" ")
        if len(split) == 1 and split[0] not in self.classnames:
            print("** class does not exist **")
        elif len(split) == 0 or split[0] in self.classnames:
            for instance in models.storage.all().values():
                print(instance)

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change into the JSON file
        """
        clsname, identity, atrname, atrvalue = line.split(" ")
        if clsname is None:
            print("** class name missing **")
        elif "BaseModel" not in line:
            print("** class does not exist **")
        else:
            id_pattern = r"[\w-]"
            id_check = re.match(id_pattern, identity)
            if id_check is None:
                print("** instance id is missing **")
            elif atrname != "email":
                print("** attribute is missing **")
            else:
                email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}"
                email_check = re.match(email_pattern, atrvalue)
                if email_check is None:
                    print("** value missing **")
                else:
                    id_check = re.match(id_pattern, identity)
                    if id_check:
                        if models.storage._storage.__object[f"{clsname}.{identity}"]:
                            instance = models.storage._storage.__object[f"{clsname}.{identity}"]
                            instance.email = atrvalue
                            models.storage._storage.__object[f"{clsname}.{identity}"] = instance
                            models.storage.save()
                        else:
                            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
