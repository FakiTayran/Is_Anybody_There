import text_ui
from text_ui import TextUI
from backpack import Backpack

class CraftHelper:
    def __init__(self):
        self.text_ui = TextUI

    def possibleCrafts(self,item1, item2):
       if((item1=="cable" and item2 == "small_metal_part")):
            if(self.inventoryCheck(item1, item2)):
                self.resultOfCrafting(item1, item2, "keylock")
       elif(True):
            return
       else:
           self.text_ui.print_command("There is no possible craft in the craft list")

    def inventoryCheck(self,item1,item2):
        backpackItems = Backpack.getItems()
        item1InBackpack = [i for i in backpackItems if i["name"] == item1.name]
        item2InBackpack = [i for i in backpackItems if i["name"] == item2.name]
        if (((item1 is not None and item1["number"] > item1InBackpack["number"]) and (item2 is not None and item2["number"] > item2InBackpack["number"]))):
            self.text_ui.print_command("Craft Successful...")
            return True
        else:
            self.text_ui.print_command("Not enough item for crafting...")
            return False
    def resultOfCrafting(item1,item2,resultItem):
        Backpack.remove_item(item1)
        Backpack.remove_item(item2)
        Backpack.add_item(resultItem)






