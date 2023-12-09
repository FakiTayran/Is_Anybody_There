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
import logging





class Game:

    def __init__(self):
        """
        Initializes the 'Adventure World' game. This constructor sets up the initial
        game settings, creates the rooms, initializes the player character, and
        prepares the game environment.
        """
        self.textUI = TextUI()
        self.createHero()
        self.create_rooms()
        self.current_room = self.capsul
        self.previous_room = None
        self.hard = False
        self.hardlevel = 0
        self.loadGameSetting()


    def createInteractiveItems(self):
        try:
            """
                   Creates interactive items in the game. Each interactive item has a name,
                   contains a list of items, and may require a password for access.
            """

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
        except Exception as e:
            self.textUI.print_command(f"Error createInteractiveItems: {str(e)}")
            logging.error(f"Error createInteractiveItems: {str(e)}")
    def create_rooms(self):
        try:
            """
            Sets up all the rooms in the game. This method initializes each room with a
            description, interactive items, required items for entry, a password if necessary,
            and a help message for the player.
            """
            self.createInteractiveItems()

            self.capsul = Room("an overturned and damaged cryonics capsul",None,None,None,None,"You can try to 'go up' to get out from capsul. You need luck to open capsul.A piece of stone from the collapsed building has fallen on you, you have to move it.",None)
            self.storage = Room("destroyed cryonics capsules warehouse",[self.capsul1,self.capsul2,self.wardrobe1,self.wardrobe2],None, 90, None,f"You can use 'search command' try to search interactive items.Maybe you can find some way to get out from this shit place",None)
            self.corridor = Room("corridor",None,["crowbar"], 90, None,'You are alone in this huge building try to pick one door to get in',None)
            self.lab = Room("cryonics lab",[self.stretcher,self.dead_body1,self.dead_body2],None, None, 1241,'Try to search everything in room',None)
            self.surgery = Room("surgery",[self.dead_body3], ["access_card"], None, None,"You can write backpack to see your items in backbag",Enemy("Zombie",30,5,None,50))
            self.office = Room("the computing admin office",[self.dead_body4],["access_card"], None, self.user.birthday,"You have to fixed manager's office key",None)
            self.managerOffice = Room("manager office",[self.safe_case],["manager_office_key"], None, None,"We can try to open safe case. Try think simple.",None)
            self.stairs = Room("building stairs",[self.dead_body5], ["keylock"], None, None,"One more dead body. Try to search. It smells shit.",None)
            self.lobby = Room("lobby",None,None, None, None,"You have to prey to stay alive good luck.",Enemy("Boss",400,100,"building_key",80))
            self.outside = Room("nothing",None, ["building_key"], None,None,"You need more help that I gave.",None)

            self.setExits()
        except Exception as e:
            self.textUI.print_command(f"Error create_rooms: {str(e)}")
            logging.error(f"Error create_rooms: {str(e)}")

    def setExits(self):
        try:

            """
                   Defines the exits for each room. This method links rooms together by specifying
                   which room is accessible from each exit direction.
            """
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
        except Exception as e:
            self.textUI.print_command(f"Error setExits: {str(e)}")
            logging.error(f"Error setExits: {str(e)}")

    def play(self):
        try:

            """
            The main gameplay loop. This method repeatedly prompts the player for input,
            processes the input commands, and continues until the game ends.
            """

            self.print_welcome()

            finished = False
            while not finished:
                command = self.textUI.get_command()  # Returns a 2-tuple
                finished = self.process_command(command)


            print("Thank you for playing!")
        except Exception as e:
            self.textUI.print_command(f"Error play: {str(e)}")
            logging.error(f"Error play: {str(e)}")

    def createHero(self):
        try:

            """
                    Initializes the hero character for the game. This method prompts the player
                    to input the name and birthday for their character, and creates a Hero object.
            """

            backpack = Backpack(10)
            hero = Hero("", backpack)
            self.user = hero

            self.user.NickName = input("Write your name... \n")
            while self.user.birthday is None or "":
                self.user.birthday = input("Write your birthday with exact that format 'MMDDYYYY'... \n")
                return

            self.textUI.print_story("A live subject was prepared...")
            while len(self.user.NickName.strip()) < 2:
                self.textUI.print_command("Min 2 characters required!")
                self.user.NickName = input("Write your name... \n")
            return self.user.NickName
        except Exception as e:
            self.textUI.print_command(f"Error createHero: {str(e)}")
            logging.error(f"Error createHero: {str(e)}")

    def loadGameSetting(self):
        try:

            """
                    Loads game settings based on player input. This method allows the player to choose
                    the difficulty level of the game and sets the game accordingly.
            """

            mode = input("Press 'H' or write 'Hard' if you want hard level game or skip with any button\n")
            if mode == 'H'.lower() or mode == 'Hard'.lower():
                self.hard = True
                hardlevel = input("Input hard level from 1 to 10\n")
                self.hardlevel = hardlevel
            else:
                self.hard = False
        except Exception as e:
            self.textUI.print_command(f"Error loadGameSetting: {str(e)}")
            logging.error(f"Error loadGameSetting: {str(e)}")

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
        return ['help', 'go', 'quit','showexits',"search",'backpack','craft',"showpossiblecrafts"]

    def process_command(self, command):
        try:
            logging.info(f"User command {command}  ")

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
            elif command_word == "SHOWPOSSIBLECRAFTS":
                mainHelper = MainHelper()
                self.textUI.print_command(mainHelper.getPossibleCraft())
            else:
                # Unknown command...
                self.textUI.print_command("Don't know what you mean.")

            return want_to_quit
        except Exception as e:
            self.textUI.print_command(f"Error process_command: {str(e)}")
            logging.error(f"Error process_command: {str(e)}")

    def print_help(self):
        try:
            """
                Display some useful help text.
            :return: None
            """
            self.textUI.print_story(f"{self.current_room.helpMessage}")
            self.textUI.print_command(f'Your command words are: {self.show_command_words()}.')
        except Exception as e:
            self.textUI.print_command(f"Error print_help: {str(e)}")
            logging.error(f"Error print_help: {str(e)}")

    def do_craft_command(self,second_word,third_word):
        try:
            if second_word is None or third_word is None:
                self.textUI.print_command("Craft what?")
                return

            if third_word is None or "":
                self.textUI.print_command("Craft with what ? ")
                return

            mainHelper = MainHelper()
            mainHelper.crafting(second_word,third_word,self.user.backpack)
        except Exception as e:
            self.textUI.print_command(f"Error do_craft_command: {str(e)}")
            logging.error(f"Error do_craft_command: {str(e)}")
    def do_search_command(self, second_word):
        try:
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
                            if str(password) != str(matching_item.password):
                                self.textUI.print_command("Think Simple...")



                if matching_item:
                    for content_item in matching_item.contains:
                        self.textUI.print_command(f"Found {content_item}")
                        if self.addBagPermisson():
                            item_removed = matching_item.removeContentFromInteractiveItemList(content_item)
                            if item_removed:
                                self.user.backpack.contents.append(content_item)
                                self.textUI.print_command(f"{content_item} was put into the bag")
                            else:
                                self.textUI.print_command(f"Could not remove {content_item} from {matching_item.name}")

                    if len(matching_item.contains) == 0:
                        self.textUI.print_command("There is no or no more item to collect")
                else:
                    self.textUI.print_command(f"No item with the name {second_word} found.")
            else:
                self.textUI.print_command(f"No item with the name {second_word} found.")
        except Exception as e:
            self.textUI.print_command(f"Error do go command: {str(e)}")
            logging.error(f"Error do search command: {str(e)}")

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        try:
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
                        if self.hard:
                            if self.user.health > 0:
                                answer = "y"
                                while answer == "y" :
                                    if self.user.health <= 0:
                                        self.textUI.print_story(f"You were brutally murdered")
                                        self.textUI.print_story("Thank you for playing.")
                                        exit()
                                    if main_helper.rollDice(False,next_room.requiredDice) >= next_room.requiredDice:
                                        self.textUI.print_command(f"Success... You are in the {next_room.description}")
                                        exitPermission = True
                                        answer = "n"
                                    else:
                                        self.user.health -= 1
                                        self.textUI.print_command(f'Health = {self.user.health}')
                                        exitPermission = False
                                        answer = input("if you want to try one more time press y\n")



                        else:
                            if main_helper.rollDice(roll_again_permission=True, requiredDice=next_room.requiredDice) >= next_room.requiredDice:
                                self.textUI.print_command(f"Success... You are in the {next_room.description}")
                                exitPermission = True
                            else:
                                self.textUI.print_command("Failed...")
                                return

            if next_room.requiredDice is None and next_room.roomPassword is None and next_room.requiredItems is None:
                exitPermission = True

            if exitPermission:
                self.previous_room = self.current_room
                self.current_room = next_room
                self.fight()
                self.current_room.requiredDice = None
                logging.info(f"User pass to {self.current_room.description}  ")

                self.textUI.print_command(self.current_room.get_long_description())
                if self.current_room == self.outside:
                    self.textUI.print_story(" a young girl is next to you, a middle-aged man is looking at you. \n")
                    self.textUI.print_story(" Young Girl(terrified) :  what happened? \n")
                    self.textUI.print_story(".........................................")
                    self.textUI.print_story("Is Anybody There is over. Thanks for playing. See you in the 2nd game.")
                    exit()



            else:
                self.textUI.print_command("No Permission")

        except Exception as e:
            self.textUI.print_command(f"Error do go command: {str(e)}")
            logging.error(f"Error do go command: {str(e)}")

            return False

    def fight(self):
        try:
            if self.hard:
                if self.current_room.enemy is not None:
                    self.textUI.print_story(f"You met the {self.current_room.enemy.name} to fight")
                    logging.info(f"User met the {self.current_room.enemy.name} to fight")
                    main_helper = MainHelper()
                    while self.current_room.enemy.health >= 0:
                        if self.user.health > 0:
                            self.textUI.print_story("Dice for us")
                            diceforUser = main_helper.rollDice(roll_again_permission=False,
                                                               requiredDice=self.current_room.requiredDice)
                            self.textUI.print_story(f" Dice for us : {diceforUser}")
                            if diceforUser > int(self.current_room.enemy.level):
                                self.textUI.print_story("Critic Hit ! 4X")
                                self.current_room.enemy.health -= (4 * diceforUser)
                            else:
                                self.current_room.enemy.health -= diceforUser

                            diceforEnemy = main_helper.rollDice(roll_again_permission=False,
                                                                requiredDice=self.current_room.requiredDice)
                            self.textUI.print_story(f" Dice for enemy : {diceforEnemy}")

                            if diceforEnemy > diceforUser:
                                self.user.health -= diceforEnemy / 10 * int(self.hardlevel)
                            else:
                                self.user.health -= self.current_room.enemy.damage
                        else:
                            self.textUI.print_story("You were brutally murdered")
                            self.textUI.print_story("Thank you for playing.")
                            exit()

                    if self.current_room.enemy.loot is None:
                        self.textUI.print_story(f"There is no item to loot from {self.current_room.enemy.name} ")
                    else:
                        for item in self.current_room.enemy.loot:
                            if self.addBagPermisson:
                                self.user.backpack.add_item(item)
                                self.textUI.print_story(f"You dropped {item.name} from {self.current_room.enemy.name} ")

                    self.textUI.print_story(f"You destroyed {self.current_room.enemy.name}")
                    self.current_room.enemy = None

        except Exception as e:
            self.textUI.print_command(f"Error in fight: {str(e)}")
            logging.error(f"Error in fight: {str(e)}")

            return False

    def addBagPermisson(self):
        try:
            answer = input("Do you want to add this item into your bag  (yes/no) or (y/n)? \n")
            if answer.lower() == "yes" or answer.lower() == "y":
                return True
            else:
                return False
        except Exception as e:
            self.textUI.print_command(f"Error in addBagPermisson: {str(e)}")
            logging.error(f"Error checking items in backpack: {str(e)}")


            return False
def main():
    # Configure the logging
    logging.basicConfig(filename='game.log',
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    game = Game()
    game.play()


if __name__ == "__main__":
    main()

