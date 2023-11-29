"""
A simple text based User Interface (UI) for the Adventure World game.
"""
import time



class TextUI:

    def __init__(self):
        # Nothing to do...
        pass

    def get_command(self):
        """
            Fetches a command from the console.
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        word3 = None
        print('> ', end='')
        input_line = input()
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 2:
                word3 = all_words[2]

            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2,word3)

    def print_command(self, text):
        """
            Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        print(text)

    def print_story(self, text):
        """
            Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        for char in text:
            print(char, end='')
            time.sleep(0.05)  # there is a 0.5 second for each word

        print('\n')