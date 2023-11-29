import text_ui
from text_ui import TextUI

class CraftHelper:
    def __init__(self):
        self.text_ui = TextUI()

    def possibleCrafts(self,item1, item2,backpack):
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

    def inventoryCheck(self,item1,item2,backpack):
        item1InBackpack = backpack.check_item(item1)
        item2InBackpack = backpack.check_item(item2)
        if (item1InBackpack and item2InBackpack):
            self.text_ui.print_command("Craft Successful...")
            return True
        else:
            self.text_ui.print_command("Not enough item for crafting...")
            return False
    def resultOfCrafting(self,item1,item2,resultItem,backpack):
        backpack.remove_item(item1)
        backpack.remove_item(item2)
        backpack.add_item(resultItem)
        print(f'You crafted a {resultItem}')






