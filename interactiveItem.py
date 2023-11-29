from item import Item  # Item sınıfını içe aktarır

class InteractiveItem(Item):
    def __init__(self, name, contains,password):
        super().__init__(name)
        self.contains = contains
        self.password = password

