from fish import Fish
from plot_fishes import *
import random
import math
from pond import Pond
from tqdm import tqdm
from write_status import Outfile

def __main__():
    random.seed() 
    tstep = 0

    pond = Pond(100,100,10)
    fishes = pond.fish_list

    outfile = Outfile(fishes)
    outfile.addFish(fishes,tstep)


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
        outfile.addFish(fishes,tstep)

    


    #my_plot.save()

__main__()
