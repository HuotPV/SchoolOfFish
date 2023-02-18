from fish import Fish
from plot_fishes import *
import random
import math
from pond import Pond
from tqdm import tqdm

def __main__():
    random.seed() 
    tstep = 0

    pond = Pond(50,50,2)
    fishes = pond.fish_list

    my_plot = FishPlot(pond)

    for fish in fishes:
        my_plot.addFish(fish)
    
    my_plot.addFishBudget(pond)
    my_plot.saveExit(tstep)

    for i in tqdm (range (2000), desc="Running simulation..."):
        my_plot = FishPlot(pond)

        for fish in fishes:
            if fish.isalive == 1:
                fish.actions(pond)
                fish.update()


        for fish in fishes:
            if fish.isalive == 1:
                my_plot.addFish(fish) 
                fish.updatePosition(1)

        pond.updateCount()
        my_plot.addFishBudget(pond)

        tstep = tstep + 1
        my_plot.saveExit(tstep)
    


    #my_plot.save()

__main__()
