"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    reads a list of words from a given file and can return a random word from that list
    
    >>> wf = WordFinder("words.txt")
    3 words read

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
        self.file = open(path)
        self.line_count = self.lines()
    
    def lines(self):
        lines = 0
        for line in self.file:
            lines += 1
        return lines