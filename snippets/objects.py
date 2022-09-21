from random import randrange

class Bombo:

    def __init__(self, initial=[]):
        self.data = initial

    def put(self, element):
        self.data.append(element)
    
    def pop(self):
        self.data.pop(randrange(0, len(self.data)))

