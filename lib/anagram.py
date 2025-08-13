# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        """
        Return a list of words from 'words' that are anagrams of self.word.
        """
        sorted_word = sorted(self.word)
        return [
            w for w in words
            if sorted(w.lower()) == sorted_word and w.lower() != self.word
        ]
