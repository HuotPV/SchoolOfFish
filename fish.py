import random
import math
import itertools

class Fish:

    id_iter = itertools.count()

    def __init__(self, test = False):
        if not test:
            self.id = next(Fish.id_iter)
            self.pos_x = random.random()*100 - 50
            self.pos_y = random.random()*100 - 50
            self.orientation = random.random()*360
        else:
            # test case, use predetermined initial condition
            self.id = next(Fish.id_iter)
            self.pos_x = 0
            self.pos_y = self.id*10
            self.orientation = 0 #random.random()*360

        self.velocity = 5
        self.aim_radius = 60.0
        self.repel_radius = 10.0
        self.color = [random.random(),random.random(),random.random()]



    def randomMotion(self):
        # add a random change to the fish orientation
        self.orientation = self.orientation + random.gauss(0,20)



    def aimFish(self,fish):
        print('Fish {} aims fish {}.'.format(self.id,fish.id))
        # add a random change to the fish orientation
        self.orientation = (self.orientation + self.getWeightAttract(fish) * self.getAngle(fish))


    def avoidFish(self,fish):
        print('Fish {} avoids fish {}.'.format(self.id,fish.id))
        # add a random change to the fish orientation
        self.orientation = (self.orientation + self.getWeightRepel(fish) * self.getAngle(fish))

    def updateLocation(self):
        # calculate new x and y coordinates from previous coord. using velocity and orientation.
        self.pos_x = self.pos_x + math.cos( (self.orientation * math.pi) / 180) * self.velocity
        self.pos_y = self.pos_y + math.sin( (self.orientation * math.pi) / 180) * self.velocity



    def printFish(self):
        # print every information about this fish
        print('Fish {}, x: {:.2f}, y: {:.2f}, orientation: {:.2f}, velocity: {:.2f}'.format(self.id, self.pos_x, self.pos_y, self.orientation, self.velocity))



    def printFishCoords(self):
        # return fish coordinates
        return self.pos_x, self.pos_y



    def getAngle(self,fish):
        # get the direction of a neighbourhing fish
        x_dist = fish.pos_x - self.pos_x 
        y_dist = fish.pos_y - self.pos_y

        if x_dist >= 0 and y_dist >= 0 :
            theta = math.acos((x_dist / math.sqrt(x_dist*x_dist + y_dist*y_dist)) ) * 180 / math.pi
        if x_dist < 0 and y_dist >= 0 :
            theta = math.acos(x_dist / math.sqrt(x_dist*x_dist + y_dist*y_dist)) * 180 / math.pi + 90
        if x_dist < 0 and y_dist < 0 :
            theta = math.acos(x_dist / math.sqrt(x_dist*x_dist + y_dist*y_dist)) * 180 / math.pi + 180
        if x_dist >= 0 and y_dist < 0 :
            theta = math.acos(x_dist / math.sqrt(x_dist*x_dist + y_dist*y_dist)) * 180 / math.pi + 270

        return theta



    def getWeightAttract(self,fish):
        # return a number used to weight the direction change
        dist = self.getDistance(fish)
        weight = 1/(self.aim_radius - dist) / 5 
        return weight

    def getWeightRepel(self,fish):
        # return a number used to weight the direction change
        dist = self.getDistance(fish)
        weight = -1 * 1 / (self.repel_radius - dist) 
        return weight


    def getDistance(self,fish):
        # calculate the distance between two fish
        x_dist = self.getXDist(fish)
        y_dist = self.getYDist(fish)
        return math.sqrt(x_dist*x_dist + y_dist*y_dist)



    def getXDist(self,fish):
        # calculate the distance between two fish
        x_dist = self.pos_x - fish.pos_x
        return x_dist
    


    def getYDist(self,fish):
        # calculate the distance between two fish
        y_dist = self.pos_y - fish.pos_y    
        return y_dist