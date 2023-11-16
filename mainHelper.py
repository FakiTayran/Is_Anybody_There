import random
from craftHelper import CraftHelper

class MainHelper:

    def rollDice(self,roll_again_permission,requiredDice):
        min_value = 1
        max_value = 100
        roll_again = "yes"
        returnedValue = -1
        while roll_again == "yes" or roll_again == "y":
            print("Rolling the dices...")
            returnedValue = random.randint(min_value, max_value)
            print(f"The values are.... : {returnedValue}")
            if returnedValue >= requiredDice:
                return returnedValue
            if roll_again_permission:
                roll_again = input("Press 'y' or 'yes' to roll the dices again.")
            else:
                roll_again = "No"
        return returnedValue

    def crafting(self,item1,item2):
        craftHelper = CraftHelper()
        return craftHelper.possibleCrafts(item1,item2)


