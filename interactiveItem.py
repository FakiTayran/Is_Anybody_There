from item import Item  # Importing the Item class



class InteractiveItem(Item):
    """
    This class represents interactive items in the game. It extends the Item class,
    adding the capability to contain other items and potentially be secured with a password.

    Attributes:
        contains (list): A list of items (strings) contained within this interactive item.
        password (str or None): An optional password required to interact with the item.
    """
    def __init__(self, name, contains, password):
        super().__init__(name)
        self.contains = contains
        self.password = password

    def removeContentFromInteractiveItemList(self, item_name):
        """
        Attempts to remove an item from the list of contents of this interactive item.

        :param item_name: The name of the item to be removed from the contents.
        :return: True if the item was successfully removed.
        :raises: ItemNotFoundError if the item is not found in the contents.
        """
        if item_name not in self.contains:
            raise ItemNotFoundError(item_name)
        self.contains.remove(item_name)
        return True

class ItemNotFoundError(Exception):
    """
    An exception raised when an item is not found in the interactive item's contents.
    """
    def __init__(self, item_name):
        self.item_name = item_name
        super().__init__(f"Item '{item_name}' not found in the interactive item.")

    def __str__(self):
        return f"ItemNotFoundError: {self.item_name} not found."