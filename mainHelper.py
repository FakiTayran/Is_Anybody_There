import random
from craftHelper import CraftHelper

class MainHelper:
    """
        This class provides various utility functions that assist in the gameplay.
        It includes methods for rolling dice and crafting items, enhancing the game's interactivity.
    """
    def rollDice(self,roll_again_permission,requiredDice):
        """
            Simulates the rolling of a dice with values ranging from 1 to 100.
            Can optionally repeat the rolling based on player's choice.
            :param roll_again_permission: Boolean indicating if the player is allowed to roll again.
            :param requiredDice: The target number that needs to be met or exceeded for a successful roll.
            :return: The value obtained from the dice roll.
        """
        min_value = 1
        max_value = 100
        roll_again = "yes"
        returnedValue = -1
        while roll_again == "yes" or roll_again == "y":
            print("Rolling the dices...")
            returnedValue = random.randint(min_value, max_value)
            print(f"The values are.... : {returnedValue}")
            if requiredDice is not None:
                if returnedValue >= requiredDice:
                    print("Success...")
                return returnedValue
            if roll_again_permission:
                print("Unlucky...")
                roll_again = input("Press 'y' or 'yes' to roll the dices again.")
            else:
                roll_again = "No"
        return returnedValue

    def crafting(self,item1,item2,backpack):
        """
            Facilitates the crafting of items by utilizing the CraftHelper class.

            :param item1: The name of the first item to be used in crafting.
            :param item2: The name of the second item to be used in crafting.
            :param backpack: The backpack object containing the player's items.
            :return: The result of the crafting attempt.
        """
        craftHelper = CraftHelper()
        return craftHelper.possibleCrafts(item1,item2,backpack)

    def getPossibleCraft(self):
        """
            Retrieves a list of possible crafting combinations from the CraftHelper class.
            :return: A list of strings, each representing a possible crafting combination.
        """
        craftHelper = CraftHelper()
        return craftHelper.possibleCrafts()

