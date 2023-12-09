from item import Item  # Item sınıfını içe aktarır

class InteractiveItem(Item):
    """
       This class represents interactive items in the game. It extends the Item class,
       adding the capability to contain other items and potentially be secured with a password.

       Attributes:
           contains (list): A list of items (strings) contained within this interactive item.
           password (str or None): An optional password required to interact with the item.
    """
    def __init__(self, name, contains,password):
        super().__init__(name)
        self.contains = contains
        self.password = password

    def removeContentFromInteractiveItemList(self, item_name):
        """
               Attempts to remove an item from the list of contents of this interactive item.

               :param item_name: The name of the item to be removed from the contents.
               :return: True if the item was successfully removed, False if the item was not found.
        """
        if item_name in self.contains:
            self.contains.remove(item_name)
            return True
        else:
            return False