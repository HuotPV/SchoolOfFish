from fish import Fish
from schooloffish import SchoolOfFish, SchoolOfIdenticalFish
from plot_fishes import *
import random
import math
from tqdm import tqdm

def __main__():
    random.seed() 
    tstep = 0

    school = SchoolOfFish(50,50,2)
    fishes = school.fish_list
    blue_fishes, red_fishes, carnivorous_fishes = school.groupFishPerType()


    school_of_blue_fishes = SchoolOfIdenticalFish(blue_fishes)
    school_of_red_fishes = SchoolOfIdenticalFish(red_fishes)
    school_of_carnivorous_fishes = SchoolOfIdenticalFish(carnivorous_fishes)

    my_plot = FishPlot()

    for fish in fishes:
        my_plot.addFish(fish)
        #my_plot.addZones(fish)
    
    my_plot.addFishBudget(school)
    my_plot.saveExit(tstep)

    for i in tqdm (range (2000), desc="Running simulation..."):
        my_plot = FishPlot()

        for fish in fishes:
            if fish.isalive == 1:
                fish.randomMotion()

                neighbour_carnivorous_fish = school.listCarnivorousFishNeighbours(fish)

                if fish.type == 'RedFish':
                    neighbour_fish = school_of_red_fishes.listFishNeighbours(fish)
                    group_fish = school_of_red_fishes.listFishGroup(fish)
                    tooclose_fish = school_of_red_fishes.listFishTooClose(fish)
                elif fish.type == 'BlueFish':
                    neighbour_fish = school_of_blue_fishes.listFishNeighbours(fish)
                    group_fish = school_of_blue_fishes.listFishGroup(fish)
                    tooclose_fish = school_of_blue_fishes.listFishTooClose(fish)
                elif fish.type == 'CarnivorousFish':
                    neighbour_fish = school.listFishNeighbours(fish)
                    group_fish = school.listFishGroup(fish)
                    tooclose_fish = school.listFishTooClose(fish)

                fish.number_in_neighbourhood = len(neighbour_fish)

                for nfish in neighbour_fish:
                    fish.aimFish(nfish)
                fish.number_in_group = len(group_fish)
                for gfish in group_fish:
                    fish.imitateFish(gfish)
                for cfish in tooclose_fish:
                    fish.avoidFish(cfish)
                for ffish in neighbour_carnivorous_fish:
                    fish.fleeFish(ffish)
        
        school.updateCount()

        for fish in fishes:
            if fish.isalive == 1:
                fish.update()
                my_plot.addFish(fish) 
                #my_plot.addZones(fish)
                fish.updatePosition(1)

        my_plot.addFishBudget(school)

        tstep = tstep + 1
        my_plot.saveExit(tstep)
    


    #my_plot.save()

__main__()
