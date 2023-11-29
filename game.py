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
from enemy import Enemy
import time


class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.textUI = TextUI()
        self.createHero()
        self.create_rooms()
        self.current_room = self.capsul
        self.previous_room = None
        self.hard = True

    def createInteractiveItems(self):
        self.capsul1 = InteractiveItem("capsul1", ["manager_office_key_part2"],None)
        self.capsul2 = InteractiveItem("capsul2", ["A note contains number (1241)"],None)
        self.wardrobe1 = InteractiveItem("wardrobe1", ["key"],None)
        self.wardrobe2 = InteractiveItem("wardrobe2", ["crowbar"],None)

        self.stretcher = InteractiveItem("stretcher", ["sheet", "pillow"],None)
        self.dead_body1 = InteractiveItem("dead_body1", ["note", "cable"],None)
        self.dead_body2 = InteractiveItem("dead_body2", ["access_card","A note, that says 'I love you dad'"],None)
        self.dead_body3 = InteractiveItem("dead_body3", ["A picture with an adult man and a young girl, that is also includes a note under them.'Happy birthday dad'"],None)
        self.dead_body4 = InteractiveItem("dead_body4",["manager_office_key_part1"],None)
        self.safe_case = InteractiveItem("safe_case", ["gun","£10000",'small_gun_part'],123456)
        self. dead_body5 = InteractiveItem("dead_body5", ["bullet"],None)
    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.createInteractiveItems()

        self.capsul = Room("an overturned and damaged cryonics capsul",None,None,None,None,"You can try to 'go up' to get out from capsul. You need luck to open capsul.A piece of stone from the collapsed building has fallen on you, you have to move it.",None)
        self.storage = Room("destroyed cryonics capsules warehouse",[self.capsul1,self.capsul2,self.wardrobe1,self.wardrobe2],None, 90, None,f"You can use 'search command' try to search interactive items.Maybe you can find some way to get out from this shit place",None)
        self.corridor = Room("corridor",None,["crowbar"], 90, None,'You are alone in this huge building try to pick one door to get in',None)
        self.lab = Room("cryonics lab",[self.stretcher,self.dead_body1,self.dead_body2],None, None, 1241,'Try to search everything in room',None)
        self.surgery = Room("surgery",[self.dead_body3], ["access_card"], None, None,"You can write backpack to see your items in backbag",None)
        self.office = Room("the computing admin office",[self.dead_body4],["access_card"], None, self.user.birthday,"You have to fixed manager's office key",None)
        self.managerOffice = Room("manager office",[self.safe_case],["manager_office_key"], None, None,"We can try to open safe case. Try think simple.",None)
        self.stairs = Room("building stairs",[self.dead_body5], ["keylock"], None, None,"One more dead body. Try to search. It smells shit.",None)
        self.lobby = Room("lobby",None,None, None, None,"You have to prey to stay alive good luck.")
        self.outside = Room("nothing",None, ["building_key"], None,None,"You need more help that I gave.",Enemy("Kaladdune",100,10))

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
        while self.user.birthday is None or "":
            self.user.birthday = input("Write your birthday with exact that format 'MMDDYYYY'... \n")
            return
        mode = input("Press 'H' or write 'Hard' if you want hard level game")
        if mode == 'H'.lower() or 'Help'.lower():
            self.hard = True
        self.textUI.print_story("A live subject was prepared...")
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
        return ['help', 'go', 'quit','showexits',"search",'backpack','craft']

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word, third_word = command
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
        elif command_word == "CRAFT":
            self.do_craft_command(second_word,third_word)

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

    def do_craft_command(self,second_word,third_word):
        if second_word is None or third_word is None:
            self.textUI.print_command("Craft what?")
            return

        if third_word is None or "":
            self.textUI.print_command("Craft with what ? ")
            return

        mainHelper = MainHelper()
        mainHelper.crafting(second_word,third_word,self.user.backpack)

    def do_search_command(self, second_word):

        if second_word is None:
            self.textUI.print_command("Search what?")
            return


        if second_word in [item.name for item in self.current_room.interactiveItems if hasattr(item, "name")]:
            self.textUI.print_story(f"Searching {second_word}...")

            matching_item = next((item for item in self.current_room.interactiveItems if
                                  hasattr(item, "name") and item.name == second_word), None)

            if matching_item.password is not None:
                password = input("Password 6 number\n")

                while str(password) != str(matching_item.password):
                    again = input("Input Y or YES if you want to try again\n").lower()
                    if again != 'Y'.lower() or 'YES'.lower():
                        password = input("Password 6 number\n")
                        if password != matching_item.password:
                            self.textUI.print_command("Think Simple...")



            if matching_item:
                for content_item in matching_item.contains:
                    self.textUI.print_command(f"Found {content_item}")
                    answer = input("Do you want to add this item into your bag  (yes/no) or (y/n)? \n")
                    if answer.lower() == "yes" or answer.lower() == "y":
                        self.current_room.interactiveItems.remove(content_item) #dolaptan itemi çıkarıyoruz
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
                if password == str(next_room.roomPassword):
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
                        if  self.hard:
                            self.user.health -= 1
                            self.textUI.print_command(f'Health = {self.user.health}')
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

