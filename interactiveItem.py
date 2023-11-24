from item import Item  # Item sınıfını içe aktarır

class InteractiveItem(Item):
    def __init__(self, name, contains):
        super().__init__(name)
        self.contains = contains

