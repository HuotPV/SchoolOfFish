from fish import *
import csv

class Pond:

    def __init__(self,bluefish,redfish,carnivorousfish):
        self.border = 200
        self.fish_list = ()
        for nf in  range(0,bluefish):
            self.fish_list = self.fish_list + (BlueFish(self),)
        for nf in  range(0,redfish):
            self.fish_list = self.fish_list + (RedFish(self),)
        for nf in  range(0,carnivorousfish):
            self.fish_list = self.fish_list + (CarnivorousFish(self),)

        self.n_bluefish = bluefish
        self.n_redfish = redfish
        self.n_carnivorousfish = carnivorousfish



    def groupFishPerType(self):
        # return lists containing a fishs with the same type
        fishes = self.fish_list
        blue_fishes = ()
        red_fishes = ()
        carnivorous_fishes = ()

        for fish in fishes:
            if fish.type == 'BlueFish':
                blue_fishes = blue_fishes + (fish,)
            elif fish.type == 'RedFish':
                red_fishes = red_fishes + (fish,)
            elif fish.type == 'CarnivorousFish':
                carnivorous_fishes = carnivorous_fishes + (fish,)

        return blue_fishes, red_fishes, carnivorous_fishes

    def updateCount(self):
        # recount the number of fish in each categories
        nb = 0
        nr = 0
        nc = 0

        for fish in self.fish_list:
            if fish.type == 'BlueFish' and fish.isalive == 1:
                nb = nb+1
            elif fish.type == 'RedFish' and fish.isalive == 1:
                nr = nr+1
            elif fish.type == 'CarnivorousFish' and fish.isalive == 1:
                nc = nc+1
        
        self.n_redfish = nr
        self.n_bluefish = nb
        self.n_carnivorousfish = nc