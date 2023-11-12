from text_ui import TextUI
from backpack import Backpack

craftParts = [{"cable": 2, None: None, None: None, "keylock": None},
              {"hardMetal": 1, "sharper": 1, "hand_made_knife": None}]


def possibleCraft(item1, numberofItem1, item2, numberofItem2):
    item1_data = None
    item2_data = None

    for part in craftParts:
        if item1 in part:
            item1_data = part
        if item2 in part:
            item2_data = part

    if item1_data is not None and item2_data is not None:
        if item1_data[item1] is not None and item1_data[item1] >= numberofItem1:
            if item2_data[item2] is not None and item2_data[item2] >= numberofItem2:
                TextUI.print_command("Crafting Successful")
                item1_data[item1] -= numberofItem1
                item2_data[item2] -= numberofItem2
            else:
                TextUI.print_command(f"Not enough {item2} ")
        else:
            TextUI.print_command(f"Not enough {item1} ")
    else:
        TextUI.print_command("The items ,that you are providing, are not inside of craft system..")


