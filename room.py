"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""


from text_ui import TextUI

class Room:
    """
        Represents a room or location in the game. Each room has a description, a list of interactive items,
        required items for entry, and potentially an enemy. The room also stores exits to other rooms.

        Attributes:
            description (str): Textual description of the room (e.g., 'kitchen', 'an open courtyard').
            interactiveItems (list): A list of InteractiveItem objects contained in the room.
            requiredItems (list): Items required to enter or interact with the room.
            requiredDice (int): Dice value required to enter the room, if any.
            roomPassword (str): Password required to enter the room, if any.
            helpMessage (str): A message providing help or hints about the room.
            enemy (Enemy): An Enemy object present in the room, if any.
            exits (dict): A dictionary mapping directions to neighboring Room objects.
            textUI (TextUI): An instance of TextUI for text-based interaction.
    """
    def __init__(self, description, interactiveItems, requiredItems, requiredDice, roomPassword,helpMessage,enemy):
        """
            Constructor method.
        :param description: Text description for this room
        """
        self.interactiveItems = interactiveItems if interactiveItems is not None else []
        self.description = description
        self.helpMessage = helpMessage

        self.requiredItems = requiredItems
        self.requiredDice = requiredDice
        self.roomPassword = roomPassword

        self.exits = {}  # Dictionary
        self.textUI = TextUI()
        self.enemy = enemy



    def set_exit(self, direction, neighbour):

        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        if direction == 'backwards':
            self.requiredDice = None

        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return f"{self.description}"

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        interactive_item_names = [item.name for item in self.interactiveItems if
                                  item is not None and hasattr(item, "name")]
        return f'Location: {self.description}, Exits: {self.get_exits()} and room includes {", ".join(interactive_item_names)}.'

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



