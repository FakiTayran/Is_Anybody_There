class Hero:
    """
        This class represents the hero (player character) in the game.
        It includes attributes such as the hero's nickname, birthday, health status,
        and a backpack for carrying items.

        Attributes:
            NickName (str): The nickname of the hero.
            birthday (str): The birthday of the hero, set to None initially and can be updated.
            health (int): The health points of the hero, starting at 100.
            backpack (Backpack): A Backpack object representing the hero's item storage.
    """
    def __init__(self,NickName,Backpack):
        self.NickName = NickName
        self.birthday = None
        self.health = 100
        self.backpack = Backpack
