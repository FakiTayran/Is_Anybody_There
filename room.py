"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""

from mainHelper import MainHelper
from backpack import Backpack
from text_ui import TextUI

class Room:

    def __init__(self, description, interactiveItems):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.description = description
        self.interactiveItems = interactiveItems
        self.exits = {}  # Dictionary
        self.textUI = TextUI()

    def set_exit(self, direction, neighbour, requiredItems, requiredDice,roomPassword):

        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

        inventory = ""
        exitPermission = False
        if roomPassword is not None:
            password = input("Input Password")
            if password == roomPassword:
                exitPermission = True
                self.exits[direction] = neighbour
            else:
                self.textUI.print_command("You need to correct password to open" + neighbour)
                exitPermission = False


        if requiredItems is not None:
            for requiredItem in requiredItems:
                if requiredItem not in inventory:
                    self.textUI.print_command("You need " + requiredItem + " to open" + neighbour + "'s door")
                    exitPermission = False
                else:
                    exitPermission = True

        main_helper = MainHelper()

        if requiredDice is not None:
            if requiredDice:
                if main_helper.rollDice(roll_again_permission=True,requiredDice=requiredDice) >= requiredDice:
                    self.textUI.print_command("Success...")
                    exitPermission = True
                else:
                    self.textUI.print_command("Failed...")
                    exitPermission = False

        if exitPermission:
            self.exits[direction] = neighbour
        else:
            self.textUI.print_command("No Permission")

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None



