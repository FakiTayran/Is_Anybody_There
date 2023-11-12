import random
import craft

def rollDice(roll_again_permission):
    min_value = 1
    max_value = 100
    roll_again = "yes"
    returnedValue = -1
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        returnedValue = random.randint(min_value, max_value)
        if roll_again_permission:
            roll_again = input("Press 'y' or 'yes' to roll the dices again.")
        else:
            roll_again = "No"
    return returnedValue

def crafting(item1,item2):
    return craft.possibleCraft(item1,item2)


