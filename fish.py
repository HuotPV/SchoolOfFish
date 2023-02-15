import random


class Fish:

    def __init__(self):
        random.seed() # maybe we should put this elsewhere ?
        self.pos_x = random.random()*10
        self.pos_y = random.random()*10
        self.velocity = 0.1
        self.orientation = random.random()*360

    def randomMotion(self):
        # add a random change to the fish orientation
        self.orientation = self.orientation + random.gauss(0,20)

