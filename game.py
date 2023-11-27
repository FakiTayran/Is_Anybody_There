"""
This class is the main class of the "Adventure World" application.
'Adventure World' is a very simple, text based adventure game. Users can walk
around some scenery. That's all. It should really be extended to make it more
interesting!

To play this game, create an instance of this class and call the "play" method.

This main class creates and initialises all the others: it creates all rooms,
creates the parser and starts the game. It also evaluates and executes the
commands that the parser returns.

This game is adapted from the 'World of Zuul' by Michael Kolling and 
David J. Barnes. The original was written in Java and has been simplified and
converted to Python by Kingsley Sage.
"""
import text_ui
from text_ui import TextUI
from room import Room
from mainHelper import MainHelper
from backpack import Backpack
from hero import Hero
from interactiveItem import InteractiveItem
import time


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_rooms()
        self.current_room = self.capsul
        self.textUI = TextUI()
        self.previous_room = None

    def createInteractiveItems(self):
        self.capsul1 = InteractiveItem("capsul1", [])
        self.capsul2 = InteractiveItem("capsul2", ["A note contains number (1241)"])
        self.wardrobe1 = InteractiveItem("wardrobe1", [])
        self.wardrobe2 = InteractiveItem("wardrobe2", ["crowbar"])

        self.stretcher = InteractiveItem("stretcher", ["sheet", "pillow"])
        self.dead_body1 = InteractiveItem("dead_body1", ["note", "key"])
        self.dead_body2 = InteractiveItem("dead_body2", ["necklace"])
        self.dead_body3 = InteractiveItem("dead_body2", ["office_key"])
        self.safe_case = InteractiveItem("safe_case", ["gun","£10000"])
        self. dead_body4 = InteractiveItem("dead_body4", ["bullet"])
    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.createInteractiveItems()

        self.capsul = Room("an overturned and damaged cryonics capsul",None,None,None,None,"You can try to 'go up' to get out from capsul. You need luck to open caqpsul.A piece of stone from the collapsed building has fallen on you, you have to move it.")
        self.storage = Room("destroyed cryonics capsules warehouse",[self.capsul1,self.capsul2,self.wardrobe1,self.wardrobe2],None, 90, None,f"You can use 'search command' try to search interactive items.Maybe you can find some way to get out from this shit place")
        self.corridor = Room("corridor",None,["crowbar"], 90, None,'You are alone in this huge building try to pick one door to get in')
        self.lab = Room("cryonics lab",[self.stretcher,self.dead_body1,self.dead_body2],["access_card"], None, 1241,'Try to search everything in room')
        self.surgery = Room("surgery",[self.dead_body3], ["access_card"], None, None,"You can pess I to open your backbag")
        self.office = Room("the computing admin office",None,["access_card"], None, 4043,"You have to find manager's office key")
        self.managerOffice = Room("manager office","safe_case",["manager_office_key"], None, None,"We can try to open safe case.")
        self.stairs = Room("building stairs",[self.dead_body4], ["keylock"], None, None,"One more dead body. Try to search. It smells shit.")
        self.lobby = Room("lobby",None,None, 100, None,"You have to prey to stay alive good luck.")
        self.outside = Room("nothing",None, ["building_key"], None,None,"You need more help that I gave.")

        self.setExits()


    def setExits(self):
        self.capsul.set_exit("up", self.storage)
        self.storage.set_exit("forward", self.corridor)
        self.corridor.set_exit("backwards", self.storage)
        self.corridor.set_exit("left", self.lab)
        self.lab.set_exit("backwards", self.corridor)
        self.corridor.set_exit("right", self.surgery)
        self.corridor.set_exit("forward", self.stairs)
        self.surgery.set_exit("backwards", self.corridor)
        self.lab.set_exit("forward", self.office)
        self.office.set_exit("backwards", self.corridor)
        self.office.set_exit("right", self.managerOffice)
        self.managerOffice.set_exit("backwards", self.office)
        self.stairs.set_exit("down", self.lobby)
        self.stairs.set_exit("up", self.corridor)
        self.lobby.set_exit("forward", self.outside)
        self.lobby.set_exit("backwards", self.stairs)

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.createHero()
        self.print_welcome()

        finished = False
        while not finished:
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)


        print("Thank you for playing!")

    def createHero(self):
        backpack = Backpack(10)
        hero = Hero("", backpack)
        self.user = hero

        self.user.NickName = input("Write your name... \n")
        while len(self.user.NickName.strip()) < 2:
            self.textUI.print_command("Min 2 characters required!")
            self.user.NickName = input("Write your name... \n")
        return self.user.NickName


    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """

        self.textUI.print_story("[A woman screaming from far away]")
        self.textUI.print_story("Is Anybody there !!!")
        self.textUI.print_story("[A man screaming from far away]")
        self.textUI.print_story("Is Anybody there !!!")

        self.textUI.print_story(f"You are realized you are in {self.capsul.description} and nobody can hear you. Focus {self.user.NickName} !!!! Focus...")
        self.textUI.print_command(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit','showexits',"search",'backpack']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
        elif command_word == "SEARCH":
            self.do_search_command(second_word)
        elif command_word == "BACKPACK":
            self.user.backpack.getItems()
        elif command_word == "SHOWEXITS":
            self.textUI.print_command(self.current_room.get_exits())
        else:
            # Unknown command...
            self.textUI.print_command("Don't know what you mean.")

        return want_to_quit

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_story(f"{self.current_room.helpMessage}")
        self.textUI.print_command(f'Your command words are: {self.show_command_words()}.')

    def do_search_command(self, second_word):
        if second_word is None:
            self.textUI.print_command("Search what?")
            return


        if second_word in [item.name for item in self.current_room.interactiveItems if hasattr(item, "name")]:
            self.textUI.print_story(f"Searching {second_word}...")

            matching_item = next((item for item in self.current_room.interactiveItems if
                                  hasattr(item, "name") and item.name == second_word), None)

            if matching_item:
                for content_item in matching_item.contains:
                    self.textUI.print_command(f"Found {content_item}")
                    answer = input("Do you want to add this item into your bag  (yes/no) or (y/n)? \n")
                    if answer.lower() == "yes" or answer.lower() == "y":
                        self.user.backpack.contents.append(content_item)
                        self.textUI.print_command(f"{content_item} was put into bag ")
                if len(matching_item.contains) == 0:
                    self.textUI.print_command("There is no item to collect")
            else:
                self.textUI.print_command(f"No item with the name {second_word} found.")
        else:
            self.textUI.print_command(f"No item with the name {second_word} found.")

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        exitPermission = False

        if second_word == None:
            # Missing second word...
            self.textUI.print_command("Go where?")
            return

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_command("There is no door!")
        else:

            if self.previous_room is not None:
                if self.previous_room == next_room:
                    self.previous_room = self.current_room
                    self.current_room = next_room
                    self.textUI.print_command(self.current_room.get_long_description())
                    return

            if exitPermission or next_room.roomPassword is not None:
                password = input("Input Password\n")
                if password == next_room.roomPassword:
                    exitPermission = True
                else:
                    self.textUI.print_command(f"You need to correct password to open next room")
                    return

            if next_room.requiredItems is not None:

                for requiredItem in next_room.requiredItems:
                    if requiredItem not in self.user.backpack.contents:
                        self.textUI.print_command(f"You need {requiredItem} to open next door")
                        return
                    else:
                        exitPermission = True

            main_helper = MainHelper()

            if next_room.requiredDice is not None:
                if next_room.requiredDice:
                    if main_helper.rollDice(roll_again_permission=True, requiredDice=next_room.requiredDice) >= next_room.requiredDice:
                        self.textUI.print_command(f"Success... You are in the {next_room.description}")
                        exitPermission = True
                    else:
                        self.textUI.print_command("Failed...")
                        return



        if exitPermission:
            self.previous_room = self.current_room
            self.current_room = next_room
            self.textUI.print_command(self.current_room.get_long_description())
        else:
            self.textUI.print_command("No Permission")



def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()

