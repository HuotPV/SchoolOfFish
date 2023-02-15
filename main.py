from fish import Fish
from schooloffish import SchoolOfFish
from plot_fishes import *
import random

def __main__():
    random.seed() # maybe we should put this elsewhere ?

    #fishes = (Fish(),Fish(),Fish(),Fish())
    fishes = (Fish(test=True),Fish(test=True),Fish(test=True),Fish(test=True))
    school = SchoolOfFish(fishes)

    my_plot = FishPlot()

    for i in range(0,15):
        for fish in fishes:
            print('I am fish {} !'.format(fish.id))
            fish.randomMotion()
            neighbour_fish = school.listFishNeighbours(fish)
            tooclose_fish = school.listFishTooClose(fish)

            print('My neighbours are:')
            for nfish in neighbour_fish:
                print('-- fish {}, distance: {:.2f}'.format(nfish.id,fish.getDistance(nfish)))
            for nfish in neighbour_fish:
                fish.aimFish(nfish)
            
            print('Fishes too close are:')
            for nfish in tooclose_fish:
                print('-- fish {}, distance: {:.2f}'.format(nfish.id,fish.getDistance(nfish)))
            for nfish in tooclose_fish:
                fish.avoidFish(nfish)

            print('-------------------------')
            my_plot.addFish(fish)
            fish.updateLocation()
    


    my_plot.save()

__main__()
