from fish import Fish

def __main__():

    fish_one = Fish()

    for i in range(0,10):
        fish_one.printFish()
        fish_one.randomMotion()
        fish_one.updateLocation()

__main__()
