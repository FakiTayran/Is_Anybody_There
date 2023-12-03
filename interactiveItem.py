from item import Item  # Item sınıfını içe aktarır

class InteractiveItem(Item):
    def __init__(self, name, contains,password):
        super().__init__(name)
        self.contains = contains
        self.password = password

    def removeContentFromInteractiveItemList(self, item_name):
        if item_name in self.contains:
            self.contains.remove(item_name)
            return True
        else:
            return False