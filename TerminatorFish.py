import fish
from fish import Fish, CarnivorousFish
import random
from random import random as rng
import math
import itertools

class TerminatorFish(CarnivorousFish):
    # One day this fish will be able to learn how to hunt by itself ...

    def __init__(self,pond, test = False):
        super().__init__(pond)
        self.speed_normal = 4
        self.speed_hunt = 10
        self.speed = 4
        self.velocity = [math.cos(self.orientation)*self.speed,math.sin(self.orientation)*self.speed]
        self.rand_strength = 1
        self.aim_radius = 60.0
        self.group_strength = 6
        self.imitate_strength = 0
        self.agora_phobia = 0
        self.color = [0,0,0]
        self.size = 8
        self.type = 'TerminatorFish'
        self.hunger_max = 100
        self.hunger = rng()*self.hunger_max
        self.danger_fear = 10
        self.is_eatable = 0

    def getEnv(self,nfishes):
        env_vector = []

        for fish in nfishes:
            env_vector.extend([fish.pos_x,fish.pos_y,fish.velocity[0],fish.velocity[1],fish.isalive,fish.is_eatable])

        return env_vector

    def actions(self,pond):
        # list of action for this type of fish
        fishes_in_neighbourhood = self.listEatableFishNeighbours(pond)

        env_vector = self.getEnv(fishes_in_neighbourhood)

        if self.hunger < self.hunger_max:
            self.randomMotion()

        if self.hunger >= self.hunger_max:
            for n_fish in fishes_in_neighbourhood:
                self.aimFish(n_fish)

    def eatFish(self,fish):

        if fish.isalive == 1:
            fish.isalive = 0
            self.hunger = 0