import fish

class SchoolOfFish:
    # a SchoolOfFish contains all the fish

    def __init__(self,fish):
        self.fish_list = fish

    def listFishNeighbours(self,fish):
        radius = 4

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:

            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                
                if dist < radius:
                    neighbour_list.append(a_fish)

            return neighbour_list


