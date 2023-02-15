from fish import Fish
from schooloffish import SchoolOfFish
from plot_fishes import *

def __main__():

    fishes = (Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish())
    school = SchoolOfFish(fishes)

    print(fishes[0].getDistance(fishes[1]))

    fish_list = school.listFishNeighbours(fishes[0])

    for fish in fish_list:
        fish.printFish()

    my_plot = FishPlot()

    for i in range(0,10):
        for fish in fishes:
            fish.randomMotion()
            my_plot.addFish(fish)
            fish.updateLocation()
    


    my_plot.save()

__main__()
