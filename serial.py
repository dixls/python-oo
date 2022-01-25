"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=0):
        """Defines serial number start as 0 by default, creates serial number list"""
        self.start = start
        self.serials = []
    
    def generate(self):
        """adds a new serial number to the end of the serials list and returns that new value"""
        self.serials.append(self.start + len(self.serials))
        return self.serials[-1]
    
    def reset(self):
        """resets serial list to empty list, thus resetting the serial start count"""
        self.serials = []




