"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """
    reads a list of words from a given file and can return a random word from that list
    
    >>> wf = WordFinder("words.txt")
    235887 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    
    """
    def __init__(self, path):
        """records the file to a list,"""
        self.file = open(path)
        self.line_list = self.file.read().split('\n')
        self.line_count = len(self.line_list)
        print(f"{self.line_count} words read")
        self.file.close()
    
    def random(self):
        """returns a random line from the line list"""
        line_num = randint(0, self.line_count)
        return self.line_list[line_num]

class SpecialWordFinder(WordFinder):
    """
    expands WordFinder to be able to parse files with comments and blanks
    """
    def __init__(self, path):
        super().__init__(path)
        self.line_list = [item for item in self.line_list if item and item[0] != "#"]
        self.line_count = len(self.line_list)
        print(f"but actually {self.line_count} words read")