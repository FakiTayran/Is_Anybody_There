class Item:
    """
       This class represents a super class for items in the game. It serves as a base class for more specific types of items.
       The primary attribute of an item is its name, which uniquely identifies it within the game context.

       Attributes:
           name (str): The name of the item.
    """
    def __init__(self,name):
        self.name = name
