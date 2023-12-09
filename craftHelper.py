import text_ui
from text_ui import TextUI

class CraftHelper:
    """
        This class provides functionalities for crafting new items by combining existing items.
        It utilizes a backpack instance to check for available items and to update the inventory
        after crafting.
    """
    def __init__(self):
        self.text_ui = TextUI()

    def getpossibleCrafts(self):
        # Returns a list of possible crafting combinations.

        return ["cable,small_gun_part : keylock","manager_office_key_part1,manager_office_key_part2 : manager_office_key", "gun,bullet : gun_with_bullet"]
    def possibleCrafts(self,item1, item2,backpack):
        #   Checks if two items can be crafted together and performs the crafting operation
        #   if possible.
        # :return: A list of strings, each representing a possible crafting combination.


       if((item1=="cable" and item2 == "small_gun_part")):
            if(self.inventoryCheck(item1, item2,backpack)):
                self.resultOfCrafting(item1, item2, "keylock",backpack)
       elif(item1=="manager_office_key_part1" and item2=="manager_office_key_part2"):
            if(self.inventoryCheck(item1, item2,backpack)):
                self.resultOfCrafting(item1, item2, "manager_office_key",backpack)
       elif (item1 == "gun" and item2 == "bullet"):
            if (self.inventoryCheck(item1, item2, backpack)):
                self.resultOfCrafting(item1, item2, "gun_with_bullet", backpack)

       else:
           self.text_ui.print_command("There is no possible craft in the craft list")
           return

    def inventoryCheck(self, item1, item2, backpack):
        """
        Checks if both items required for crafting are present in the backpack.
        :param item1: The first item to check in the backpack.
        :param item2: The second item to check in the backpack.
        :param backpack: The backpack object containing the player's items.
        :return: True if both items are in the backpack, False otherwise.
        """
        try:
            item1_in_backpack = backpack.check_item(item1)
            item2_in_backpack = backpack.check_item(item2)
            if item1_in_backpack and item2_in_backpack:
                self.text_ui.print_command("Craft Successful...")
                return True
            else:
                self.text_ui.print_command("Not enough items for crafting...")
                return False
        except Exception as e:  # Replace 'Exception' with a more specific exception if applicable
            self.text_ui.print_command(f"Error checking items in backpack: {str(e)}")
            return False

    def resultOfCrafting(self,item1,item2,resultItem,backpack):
        """
               Performs the crafting operation by removing the used items and adding the
               crafted item to the backpack.
               :param resultItem: The item resulting from the crafting.
        """
        backpack.remove_item(item1)
        backpack.remove_item(item2)
        backpack.add_item(resultItem)
        print(f'You crafted a {resultItem}')






