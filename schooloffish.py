import fish

class SchoolOfFish:
    # a SchoolOfFish contains all the fish


    def __init__(self,fish):
        self.fish_list = fish


    def listFishNeighbours(self,fish):

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:
            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                if dist < fish.aim_radius and dist >= fish.imitate_radius:
                    neighbour_list.append(a_fish)

        return neighbour_list

    def listFishGroup(self,fish):

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:
            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                if dist < fish.imitate_radius and dist >= fish.repel_radius:
                    neighbour_list.append(a_fish)

        return neighbour_list


    def listFishTooClose(self,fish):
        
        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        tooclose_list = []

        for a_fish in self.fish_list:

            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                
                if dist < fish.repel_radius:
                    tooclose_list.append(a_fish)

        return tooclose_list
