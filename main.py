from fish import Fish
from plot_fishes import *

def __main__():

    fish_one = Fish()
    my_plot = FishPlot()

    for i in range(0,10):
        fish_one.printFish()
        fish_one.randomMotion()
        my_plot.addFish(fish_one)
        fish_one.updateLocation()
    my_plot.save()

__main__()
