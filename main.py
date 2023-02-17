from fish import Fish
from schooloffish import SchoolOfFish
from plot_fishes import *
import random
import math
from tqdm import tqdm

def __main__():
    random.seed() # maybe we should put this elsewhere ?
    tstep = 0

    school = SchoolOfFish(30,15)
    fishes = school.fish_list

    my_plot = FishPlot()

    for fish in fishes:
        my_plot.addFish(fish)
        #my_plot.addZones(fish)

    my_plot.saveExit(tstep)

    for i in tqdm (range (3000), desc="Running simulation..."):
        my_plot = FishPlot()

        for fish in fishes:
            fish.randomMotion()
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
            

        for fish in fishes:
            fish.update()
            my_plot.addFish(fish) 
            #my_plot.addZones(fish)
            fish.updatePosition(1)
        
        tstep = tstep + 1
        my_plot.saveExit(tstep)
    


    #my_plot.save()

__main__()
