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


from text_ui import TextUI
from room import Room
from mainHelper import MainHelper
from backpack import Backpack
import time


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_rooms()
        self.current_room = self.capsul
        self.textUI = TextUI()

    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.capsul = Room("an overturned and damaged cryonics capsul",None,None,None,None)
        self.storage = Room("destroyed cryonics capsules warehouse",["capsul1","capsul2","Wardrobe1","Wardrobe2"],None, 90, None)
        self.corridor = Room("in a corridor",None,["crowbar"], 90, None)
        self.lab = Room("in a cryonics lab",["stretcher","dead_body1","dead_body2"],["access_card"], None, 1241)
        self.surgery = Room("in the surgery","dead_body3", ["access_card"], None, None)
        self.office = Room("in the computing admin office",None,["access_card"], None, 4043)
        self.managerOffice = Room("in the manager office","safe_case",["manager_office_key"], None, None)
        self.stairs = Room("building stairs","dead_body4", ["keylock"], None, None)
        self.lobby = Room("in the lobby","",None, 100, None)
        self.outside = Room("everywhere is destroyed",None, ["building_key"], None,None)

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
        self.managerOffice.set_exit("backwards",self.office)
        self.stairs.set_exit("down", self.lobby)
        self.stairs.set_exit("up", self.corridor)
        self.lobby.set_exit("forward", self.outside)
        self.lobby.set_exit("backwards", self.stairs)



    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)


        print("Thank you for playing!")

    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.textUI.print_story("[A woman screaming from far away]")
        self.textUI.print_story("Is Anybody there !!!")
        self.textUI.print_story("[A man screaming from far away]")
        self.textUI.print_story("Is Anybody there !!!")

        self.textUI.print_command(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'go', 'quit']

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
        else:
            # Unknown command...
            self.textUI.print_command("Don't know what you mean.")

        return want_to_quit

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_command("Open backpack , press : I")
        self.textUI.print_command("")
        self.textUI.print_command("")
        self.textUI.print_command(f'Your command words are: {self.show_command_words()}.')

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_command("Go where?")
            return

        next_room = self.current_room.get_exit(second_word)
        if next_room == None:
            self.textUI.print_command("There is no door!")
        else:

            inventory = ""
            exitPermission = False
            if next_room.roomPassword is not None:
                password = input("Input Password")
                if password == next_room.roomPassword:
                    exitPermission = True
                else:
                    self.textUI.print_command(f"You need to correct password to open next room")
                    exitPermission = False

            if next_room.requiredItems is not None:
                for requiredItem in next_room.requiredItems:
                    if requiredItem not in inventory:
                        self.textUI.print_command(f"You need {requiredItem} to open next door")
                        exitPermission = False
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
                        exitPermission = False



        if exitPermission:
            self.current_room = next_room
            self.textUI.print_command(self.current_room.get_long_description())
        else:
            self.textUI.print_command("No Permission")



def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
