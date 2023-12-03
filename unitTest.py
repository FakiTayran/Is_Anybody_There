import unittest
from unittest.mock import patch

from room import Room
from hero import Hero
from backpack import Backpack
from interactiveItem import  InteractiveItem
from mainHelper import  MainHelper
class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Room 1", None, None, None, None, "Room 1 Description", None)
        self.room2 = Room("Room 2", None, None, None, None, "Room 2 Description", None)

    def test_set_exit(self):
        self.room1.set_exit("north", self.room2)
        self.assertIn("north", self.room1.exits)
        self.assertEqual(self.room1.exits["north"], self.room2)

    def test_get_exit(self):
        # Test getting an exit
        self.room1.set_exit("north", self.room2)
        exit_room = self.room1.get_exit("north")
        self.assertEqual(exit_room, self.room2)

    def test_invalid_exit(self):
        self.assertIsNone(self.room1.get_exit("invalid_direction"))

    class TestBackpack(unittest.TestCase):

        def setUp(self):
            self.hero = Hero("Test Hero", Backpack(10))

        def test_add_item_to_backpack(self):
            self.hero.backpack.add_item("sword")
            self.assertIn("sword", self.hero.backpack.contents)
            self.assertEqual(len(self.hero.backpack.contents), 1)

        def test_remove_item_from_backpack(self):
            self.hero.backpack.add_item("shield")
            self.hero.backpack.remove_item("shield")
            self.assertNotIn("shield", self.hero.backpack.contents)

    class TestInteractiveItem(unittest.TestCase):

        def setUp(self):
            self.interactive_item = InteractiveItem("Mysterious Box", ["key", "map"], "1234")

        def test_initialization(self):
            self.assertEqual(self.interactive_item.name, "Mysterious Box")
            self.assertListEqual(self.interactive_item.contains, ["key", "map"])
            self.assertEqual(self.interactive_item.password, "1234")

        def test_remove_content_existing_item(self):
            item_removed = self.interactive_item.removeContentFromInteractiveItemList("key")
            self.assertTrue(item_removed)
            self.assertNotIn("key", self.interactive_item.contains)

        def test_remove_content_non_existing_item(self):
            item_removed = self.interactive_item.removeContentFromInteractiveItemList("compass")
            self.assertFalse(item_removed)
            self.assertNotIn("compass", self.interactive_item.contains)

    class TestMainHelper(unittest.TestCase):

        def setUp(self):
            self.main_helper = MainHelper()
            self.backpack = Backpack()

        @patch('mainHelper.random.randint')
        def test_roll_dice(self, mock_randint):
            mock_randint.return_value = 50
            result = self.main_helper.rollDice(False, 40)
            self.assertEqual(result, 50)

        def test_crafting_valid_combination(self):
            self.backpack.add_item('item1')
            self.backpack.add_item('item2')
            crafted_item = self.main_helper.crafting('item1', 'item2', self.backpack)
            self.assertIsNotNone(crafted_item)


if __name__ == '__main__':
    unittest.main()
