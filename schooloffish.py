import fish
from fish import Fish, BlueFish, RedFish, CarnivorousFish

class SchoolOfFish:
    # a SchoolOfFish contains all the fish


    #def __init__(self,fish):
        #self.fish_list = fish

    def __init__(self,bluefish,redfish,carnivorousfish):
        self.fish_list = ()
        for nf in  range(0,bluefish):
            self.fish_list = self.fish_list + (BlueFish(),)
        for nf in  range(0,redfish):
            self.fish_list = self.fish_list + (RedFish(),)
        for nf in  range(0,carnivorousfish):
            self.fish_list = self.fish_list + (CarnivorousFish(),)

        self.n_bluefish = bluefish
        self.n_redfish = redfish
        self.n_carnivorousfish = carnivorousfish
        

    def groupFishPerType(self):
        fishes = self.fish_list
        blue_fishes = ()
        red_fishes = ()
        carnivorous_fishes = ()

        for fish in fishes:
            if fish.type == 'BlueFish':
                blue_fishes = blue_fishes + (fish,)
            elif fish.type == 'RedFish':
                red_fishes = red_fishes + (fish,)
            elif fish.type == 'CarnivorousFish':
                carnivorous_fishes = carnivorous_fishes + (fish,)

        return blue_fishes, red_fishes, carnivorous_fishes


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
    

    def listCarnivorousFishNeighbours(self,fish):

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:
            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                if dist < fish.aim_radius and a_fish.type == 'CarnivorousFish' :
                    neighbour_list.append(a_fish)
        
        return neighbour_list

    def updateCount(self):
        nb = 0
        nr = 0
        nc = 0

        for fish in self.fish_list:
            if fish.type == 'BlueFish' and fish.isalive == 1:
                nb = nb+1
            elif fish.type == 'RedFish' and fish.isalive == 1:
                nr = nr+1
            elif fish.type == 'CarnivorousFish' and fish.isalive == 1:
                nc = nc+1
        
        self.n_redfish = nr
        self.n_bluefish = nb
        self.n_carnivorousfish = nc

class SchoolOfIdenticalFish(SchoolOfFish):
    # a school composed only of one type of fish
    def __init__(self,fish):
        self.fish_list = fish

    def listFishNeighbours(self,fish):

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:
            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                if dist < fish.aim_radius and dist >= fish.imitate_radius and a_fish.type == fish.type :
                    neighbour_list.append(a_fish)

        return neighbour_list

    def listFishGroup(self,fish):

        [fish_pos_x,fish_pos_y] = fish.printFishCoords()
        id = fish.id

        neighbour_list = []

        for a_fish in self.fish_list:
            if id != a_fish.id:
                dist = fish.getDistance(a_fish)
                if dist < fish.imitate_radius and dist >= fish.repel_radius and a_fish.type == fish.type :
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
