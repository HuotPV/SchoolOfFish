import random
import math
import itertools

class Fish:

    id_iter = itertools.count()

    def __init__(self):
        random.seed() # maybe we should put this elsewhere ?
        self.pos_x = random.random()*10
        self.pos_y = random.random()*10
        self.velocity = 0.1
        self.orientation = 0 # random.random()*360
        self.id = next(Fish.id_iter)
        self.color = [random.random(),random.random(),random.random()]
        

    def randomMotion(self):
        # add a random change to the fish orientation
        self.orientation = self.orientation + random.gauss(0,20)

    def updateLocation(self):
        self.pos_x = self.pos_x + math.cos( (self.orientation * math.pi) / 180)
        self.pos_y = self.pos_y + math.sin( (self.orientation * math.pi) / 180)

    def printFish(self):
        print('Fish {}, x: {:.2f}, y: {:.2f}, orientation: {:.2f}, velocity: {:.2f}'.format(self.id, self.pos_x, self.pos_y, self.orientation, self.velocity))