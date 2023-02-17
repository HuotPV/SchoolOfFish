import random
from random import random as rng
import math
import itertools

class Fish:

    id_iter = itertools.count()

    def __init__(self, test = False):
        self.border = 200

        if not test:
            self.id = next(Fish.id_iter)
            self.pos_x = rng()*self.border*2 - self.border
            self.pos_y = rng()*self.border*2 - self.border
            self.orientation = random.random()*360
        else:
            # test case, use predetermined initial condition
            self.id = next(Fish.id_iter)
            self.pos_x = 0
            self.pos_y = -30 + self.id*30
            self.orientation = 0 #random.random()*360

        self.speed = 5
        self.velocity = [math.cos(self.orientation)*self.speed,math.sin(self.orientation)*self.speed]
        self.rand_strength = 2
        self.aim_radius = 40.0
        self.group_strength = 2
        self.imitate_radius = 10.0
        self.imitate_strength = 2
        self.repel_radius = 3.0
        self.agora_phobia = 1
        self.number_in_group = 0
        self.number_in_neighbourhood = 0
        self.color = [rng(),rng(),rng()]
        self.type = 'Fish'
        self.size = 5
        self.isalive = 1
        self.danger_fear = 10



    def randomMotion(self):
        # produce a random vector with norm self.rand_strength
        rand_vel = [rng()-0.5,rng()-0.5]
        rand_vel_norm = math.sqrt(rand_vel[0]*rand_vel[0] + rand_vel[1]*rand_vel[1])
        if rand_vel_norm == 0:
            pass
        else:
            rand_vel_normalized = [x * self.rand_strength / rand_vel_norm for x in rand_vel]
            self.velocity = [self.velocity[i] + rand_vel_normalized[i] for i in range(len(self.velocity))]

    def aimCenter(self,strength):
        # produce a velocity vector getting the fish closer to the center
        center_vel = [-1 * self.pos_x,-1 * self.pos_y]
        center_vel_norm = self.getDistanceCenter()
        if center_vel_norm == 0:
            pass
        else:
            center_vel_normalized = [x * strength / center_vel_norm for x in center_vel]
            self.velocity = [self.velocity[i] + center_vel_normalized[i] for i in range(len(self.velocity))]

    def aimFish(self,fish):
        # method that modifies the velocity of a fish to get closer to a neighbourhing fish
        if fish.isalive == 1:
            fish_vel = [fish.pos_x-self.pos_x, fish.pos_y-self.pos_y]
            fish_vel_norm = self.getDistance(fish)
            if fish_vel_norm == 0:
                pass
            else:
                #fish_vel_normalized = [x * self.group_strength * self.getWeightAttract(fish) / fish_vel_norm for x in fish_vel]
                fish_vel_normalized = [x * self.group_strength / self.number_in_neighbourhood / fish_vel_norm for x in fish_vel]
                self.velocity = [self.velocity[i] + fish_vel_normalized[i] for i in range(len(self.velocity))]

    def imitateFish(self,fish):
        # imitate a fish direction
        if fish.isalive == 1:
            vel_imitate = [fish.velocity[0]-self.velocity[1], fish.velocity[1]-self.velocity[1]]
            vel_imitate_norm = self.getDistance(fish)

            if vel_imitate_norm == 0:
                pass
            else:
                vel_imitate_normalized =  [x * self.imitate_strength/self.number_in_group  / vel_imitate_norm for x in vel_imitate]
                self.velocity = [self.velocity[i] + vel_imitate_normalized[i] for i in range(len(self.velocity))]


    def avoidFish(self,fish):
        # a method that produce a vector pushing the fish away from a point
        if fish.isalive == 1:
            fish_vel = [self.pos_x - fish.pos_x, self.pos_y - fish.pos_y]
            fish_vel_norm = self.getDistance(fish)
            if fish_vel_norm == 0:
                pass
            else:
                #fish_vel_normalized = [x * self.agora_phobia * self.getWeightRepel(fish) / fish_vel_norm for x in fish_vel]
                fish_vel_normalized = [x * self.agora_phobia  / fish_vel_norm for x in fish_vel]
                self.velocity = [self.velocity[i] + fish_vel_normalized[i] for i in range(len(self.velocity))]

    def fleeFish(self,fish):
        # a method that produce a vector pushing the fish away from a point
        fish_vel = [self.pos_x - fish.pos_x, self.pos_y - fish.pos_y]
        fish_vel_norm = self.getDistance(fish)
        if fish_vel_norm == 0:
            pass
        else:
            #fish_vel_normalized = [x * self.agora_phobia * self.getWeightRepel(fish) / fish_vel_norm for x in fish_vel]
            fish_vel_normalized = [x * self.danger_fear  / fish_vel_norm for x in fish_vel]
            self.velocity = [self.velocity[i] + fish_vel_normalized[i] for i in range(len(self.velocity))]


    def updateOrientation(self):
        if self.velocity[0] >= 0 and self.velocity[1] >= 0:
            self.orientation = math.acos(abs(self.velocity[0])/self.getSpeed()) * 180 / math.pi
        elif self.velocity[0] < 0 and self.velocity[1] >= 0:
            self.orientation = 180 - math.acos(abs(self.velocity[0])/self.getSpeed()) * 180 / math.pi 
        elif self.velocity[0] < 0 and self.velocity[1] < 0:
            self.orientation = 180 + math.acos(abs(self.velocity[0])/self.getSpeed()) * 180 / math.pi 
        else:
            self.orientation = 360 - math.acos(abs(self.velocity[0])/self.getSpeed()) * 180 / math.pi


    def getSpeed(self):
        return math.sqrt(self.velocity[0]*self.velocity[0] + self.velocity[1]*self.velocity[1])

    def normalizeVelocity(self):
        norm_veloc =  self.getSpeed()
        if norm_veloc == 0:
            pass
        else:
            self.velocity = [x * self.speed / norm_veloc for x in self.velocity]


    def update(self):
        # update velocity to aim for center if needed, normalize fish velocity, update fish orientation
        # calculate new x and y coordinates from previous coord. using velocity and orientation.
        if abs(self.pos_x) > self.border or abs(self.pos_y) > self.border:
            self.aimCenter( 2 *  max( [abs(self.pos_x)/self.border, abs(self.pos_y) / self.border]))
        self.normalizeVelocity()
        self.updateOrientation()

    def updatePosition(self,dt):
        self.pos_x = self.pos_x + self.velocity[0] * dt
        self.pos_y = self.pos_y + self.velocity[1] * dt

    def printFish(self):
        # print every information about this fish
        print('Fish {}, x: {:.2f}, y: {:.2f}, orientation: {:.2f}, velocity: {:.2f}, {:.2f}'.format(self.id, self.pos_x, self.pos_y, self.orientation, self.velocity[0], self.velocity[1]))



    def printFishCoords(self):
        # return fish coordinates
        return self.pos_x, self.pos_y


    def getWeightAttract(self,fish):
        # return a number used to weight the direction change
        dist = self.getDistance(fish)
        if self.aim_radius == dist:
            weight = 0
        else:
            weight = 1/(self.aim_radius - dist)
        return weight

    def getWeightRepel(self,fish):
        # return a number used to weight the direction change
        dist = self.getDistance(fish)
        if self.repel_radius == dist:
            weight = 0
        else:
            weight = 1 * 1 / (self.repel_radius - dist) 
        return weight

    def getDistanceCenter(self):
        # calculate the distance between two fish
        x_dist = self.pos_x
        y_dist = self.pos_y
        return math.sqrt(x_dist*x_dist + y_dist*y_dist)

    def getDistance(self,fish):
        # calculate the distance between two fish
        x_dist = self.getXDist(fish)
        y_dist = self.getYDist(fish)
        return math.sqrt(x_dist*x_dist + y_dist*y_dist)

    def getAngle(self,fish):
        x_fish = fish.pos_x - self.pos_x
        y_fish = fish.pos_y - self.pos_y

        if x_fish >= 0 and y_fish >= 0:
            fish_angle = math.acos(abs(x_fish)/self.getDistance(fish)) * 180 / math.pi
        elif x_fish < 0 and y_fish >= 0:
            fish_angle = 180 - math.acos(abs(x_fish)/self.getDistance(fish)) * 180 / math.pi 
        elif x_fish < 0 and y_fish < 0:
            fish_angle = 180 + math.acos(abs(x_fish)/self.getDistance(fish)) * 180 / math.pi 
        else:
            fish_angle = 360 - math.acos(abs(x_fish)/self.getDistance(fish)) * 180 / math.pi

    def getXDist(self,fish):
        # calculate the distance between two fish
        x_dist = self.pos_x - fish.pos_x
        return x_dist

    def getYDist(self,fish):
        # calculate the distance between two fish
        y_dist = self.pos_y - fish.pos_y    
        return y_dist
    

class BlueFish(Fish):
    id_iter = itertools.count()

    def __init__(self, test = False):
        self.border = 200
        self.id = next(Fish.id_iter)
        self.pos_x = rng()*self.border*2 - self.border
        self.pos_y = rng()*self.border*2 - self.border
        self.orientation = random.random()*360
        self.speed = 5
        self.velocity = [math.cos(self.orientation)*self.speed,math.sin(self.orientation)*self.speed]
        self.rand_strength = 2
        self.aim_radius = 40.0
        self.group_strength = 2
        self.imitate_radius = 10.0
        self.imitate_strength = 2
        self.repel_radius = 3.0
        self.agora_phobia = 1
        self.number_in_group = 0
        self.number_in_neighbourhood = 0
        self.color = [rng(),rng(),rng()]
        self.color = [0.2,0.5,0.8]
        self.type = 'BlueFish'
        self.size = 5
        self.isalive = 1
        self.danger_fear = 10

class RedFish(Fish):

    id_iter = itertools.count()

    def __init__(self, test = False):
        self.border = 200
        self.id = next(Fish.id_iter)
        self.pos_x = rng()*self.border*2 - self.border
        self.pos_y = rng()*self.border*2 - self.border
        self.orientation = random.random()*360
        self.speed = 7
        self.velocity = [math.cos(self.orientation)*self.speed,math.sin(self.orientation)*self.speed]
        self.rand_strength = 3
        self.aim_radius = 30.0
        self.group_strength = 2
        self.imitate_radius = 8.0
        self.imitate_strength = 2
        self.repel_radius = 3.0
        self.agora_phobia = 1
        self.number_in_group = 0
        self.number_in_neighbourhood = 0
        self.color = [rng(),rng(),rng()]
        self.color = [0.8,0.3,0.3]
        self.type = 'RedFish'
        self.size = 4
        self.isalive = 1
        self.danger_fear = 10

class CarnivorousFish(Fish):

    def __init__(self, test = False):
        self.border = 200
        self.id = next(Fish.id_iter)
        self.pos_x = rng()*self.border*2 - self.border
        self.pos_y = rng()*self.border*2 - self.border
        self.orientation = random.random()*360
        self.speed_normal = 4
        self.speed_hunt = 10
        self.speed = 4
        self.velocity = [math.cos(self.orientation)*self.speed,math.sin(self.orientation)*self.speed]
        self.rand_strength = 1
        self.aim_radius = 60.0
        self.group_strength = 6
        self.imitate_radius = 0
        self.imitate_strength = 0
        self.repel_radius = 5
        self.agora_phobia = 0
        self.number_in_group = 0
        self.number_in_neighbourhood = 0
        self.color = [1,0.1,0]
        self.size = 8
        self.type = 'CarnivorousFish'
        self.hunger_max = 100
        self.hunger = rng()*self.hunger_max
        self.isalive = 1
        self.danger_fear = 10

    def eatFish(self,fish):
        if fish.isalive == 1:
            fish.isalive = 0
            self.hunger = 0


    def aimFish(self,fish):
        if fish.isalive == 1:

            if self.hunger > self.hunger_max:
                # method that modifies the velocity of a fish to get closer to a neighbourhing fish
                if self.getDistance(fish) < self.repel_radius:
                    self.eatFish(fish)
                else:
                    fish_vel = [fish.pos_x-self.pos_x, fish.pos_y-self.pos_y]
                    fish_vel_norm = self.getDistance(fish)
                    if fish_vel_norm == 0:
                        pass
                    else:
                        fish_vel_normalized = [x * self.group_strength / max(fish.number_in_group,1) / fish_vel_norm for x in fish_vel]
                        self.velocity = [self.velocity[i] + fish_vel_normalized[i] for i in range(len(self.velocity))]


    def update(self):
        # update velocity to aim for center if needed, normalize fish velocity, update fish orientation
        # calculate new x and y coordinates from previous coord. using velocity and orientation.
        if abs(self.pos_x) > self.border or abs(self.pos_y) > self.border:
            self.aimCenter( 2 *  max( [abs(self.pos_x)/self.border, abs(self.pos_y) / self.border]))
        self.hunger = self.hunger + 1

        if self.hunger > self.hunger_max:
            self.speed = self.speed_hunt
        else:
            self.speed = self.speed_normal 

        self.normalizeVelocity()
        self.updateOrientation()
