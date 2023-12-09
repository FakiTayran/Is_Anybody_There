class Enemy:
    """
        This class represents an enemy in a game. An enemy has attributes like name, health,
        damage potential, loot, and a level indicating its difficulty.

        Attributes:
            name : The name of the enemy.
            health : The health points of the enemy, indicating how much damage it can take before being defeated.
            damage : The damage points the enemy can inflict on the player.
            loot : The item or reward that the enemy drops when defeated.
            level : A numerical representation of the enemy's difficulty or strength.
    """
    def __init__(self,name,health,damage,loot,level):
        self.name = name
        self.health = health
        self.damage = damage
        self.loot = loot
        self.level = level
