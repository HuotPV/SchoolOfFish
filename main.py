from fish import Fish
from plot_fishes import *

def __main__():

    fishes = (Fish(),Fish(),Fish())

    my_plot = FishPlot()

    for i in range(0,10):
        for fish in fishes:
            fish.printFish()
            fish.randomMotion()
            my_plot.addFish(fish)
            fish.updateLocation()
    my_plot.save()

__main__()
