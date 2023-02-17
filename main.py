from fish import Fish
from schooloffish import SchoolOfFish
from plot_fishes import *
import random
import math

def __main__():
    random.seed() # maybe we should put this elsewhere ?
    tstep = 0


    fishes = (Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish(),Fish())
    #fishes = (Fish(test=True),Fish(test=True),Fish(test=True),Fish(test=True))

    school = SchoolOfFish(fishes)

    my_plot = FishPlot()

    for fish in fishes:
        my_plot.addFish(fish)
        #my_plot.addZones(fish)

    my_plot.saveExit(tstep)


    for i in range(0,2000):
        my_plot = FishPlot()

        for fish in fishes:
            print('I am fish {} !'.format(fish.id))

            fish.randomMotion()

            neighbour_fish = school.listFishNeighbours(fish)
            group_fish = school.listFishGroup(fish)
            tooclose_fish = school.listFishTooClose(fish)


            print('My neighbours are:')
            fish.number_in_neighbourhood = len(neighbour_fish)
            for nfish in neighbour_fish:
                print('-- fish {}, distance: {:.2f}'.format(nfish.id,fish.getDistance(nfish)))
            for nfish in neighbour_fish:
                print('-- old velocity: {:.2f}, {:.2f}'.format(fish.velocity[0],fish.velocity[1]))
                fish.aimFish(nfish)
                print('-- new velocity: {:.2f}, {:.2f}'.format(fish.velocity[0],fish.velocity[1]))

            print('My group is made of:')
            fish.number_in_group = len(group_fish)
            print(len(group_fish))
            for gfish in group_fish:
                print('-- fish {}, distance: {:.2f}'.format(gfish.id,fish.getDistance(gfish)))
            for gfish in group_fish:
                print('-- old velocity: {:.2f}, {:.2f}'.format(fish.velocity[0],fish.velocity[1]))
                fish.imitateFish(gfish)
                print('-- new velocity: {:.2f}, {:.2f}'.format(fish.velocity[0],fish.velocity[1]))
            

            print('Fishes too close are:')
            for cfish in tooclose_fish:
                print('-- fish {}, distance: {:.2f}'.format(cfish.id,fish.getDistance(cfish)))
            for cfish in tooclose_fish:
                fish.avoidFish(cfish)
                print('-- new velocity: {:.2f}, {:.2f}'.format(fish.velocity[0],fish.velocity[1]))
            
            print('-------------------------')


        for fish in fishes:

            fish.update()
            my_plot.addFish(fish) 
            #my_plot.addZones(fish)
            fish.updatePosition(1)
        
        tstep = tstep + 1
        my_plot.saveExit(tstep)
    


    #my_plot.save()

__main__()
