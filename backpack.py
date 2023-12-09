class Backpack:
    """
    This class represents a backpack which can be used to pick up and store items.
    The backpack has a limited capacity, defined at the time of creation. This class
    also demonstrates the use of a user-defined exception to handle errors.
    """

    def __init__(self, capacity):
        """
               Initializes the Backpack object with a specific capacity.

               :param capacity: An integer representing the maximum number of items the backpack can hold.
        """

        self.contents = []
        self.capacity = capacity

    def add_item(self, item):
        """
        Adds an item to the backpack if there is space available.

        :param item: The item to be added to the backpack.
        :return: True if the item was added, False if the backpack is full.
        """
        if len(self.contents) < self.capacity:
            self.contents.append(item)
            return True
        return False

    def remove_item(self, item):
        """
        Removes an item from the backpack if it is present.

        :param item: The item to be removed from the backpack.
        :raises NotInBackpackError: If the specified item is not in the backpack.
        """
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            self.contents.remove(item)
        except NotInBackpackError:
            print('Exception handled here...')
        finally:
            print('Carrying on...')

    def check_item(self, item):
        """
        Checks if an item is present in the backpack.

        :param item: The item to check for in the backpack.
        :return: True if the item is in the backpack, False otherwise.
        """
        return item in self.contents

    def getItems(self):
        """
                Prints and returns the list of items currently in the backpack.

                :return: A list of items in the backpack.
        """

        print(self.contents)
        return self.contents
class NotInBackpackError(Exception):
    """
           Initializes the NotInBackpackError with the item and error message.

           :param item: The item that caused the exception.
           :param message: A message describing the error.
    """
    def __init__(self, item, message):
        print(f'{item} {message}')


