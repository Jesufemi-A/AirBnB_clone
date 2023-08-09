#!/usr/bin/python3
"""
contains class HBNBCommand
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class to create command line interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit the commandline interpreter
        """
        exit()

    def help_quit(self):
        "Help for quit"
        print("Quit the commandline interpreter", '\n')

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
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
