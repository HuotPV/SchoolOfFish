import matplotlib as mpl
import matplotlib.pyplot as plt
import fish
from matplotlib.markers import MarkerStyle
import pathlib
import os

class FishPlot:

    def __init__(self,pond):
        self.border = pond.border
        self.axes = plt.gca()
        self.axes.set_xbound(-1.1 * self.border , 1.1 * self.border)
        self.axes.set_ybound(-1.1 * self.border , 1.1 * self.border)
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.path = os.getcwd()
        pathlib.Path(self.path + "/figures").mkdir(parents=True, exist_ok=True)


    def addFish(self,fish):
        m = MarkerStyle("^")
        m._transform.scale(0.7, 1)
        m._transform.rotate_deg(fish.orientation-90)
        self.axes.plot(fish.pos_x,fish.pos_y,marker=m, markeredgecolor = [0.1,0.1,0.1],linewidth=1, markerfacecolor = fish.color, markersize=fish.size)
        self.axes.set_ybound(-1.1 * self.border , 1.1 * self.border)
        self.axes.set_xbound(-1.1 * self.border , 1.1 * self.border)

    def addZones(self,fish):
        circle1 = plt.Circle((fish.pos_x, fish.pos_y), fish.aim_radius, color=fish.color, alpha=0.1)
        circle2 = plt.Circle((fish.pos_x, fish.pos_y), fish.imitate_radius, color=fish.color, alpha=0.5)
        circle3 = plt.Circle((fish.pos_x, fish.pos_y), fish.repel_radius, color=fish.color, alpha=0.8)
        self.axes.add_patch(circle1)
        self.axes.add_patch(circle2)
        self.axes.add_patch(circle3)

    def addFishBudget(self,pond):
        self.axes.set_title('Blue fish: {}, Red fish: {}, Carnivorous Fish: {}'.format(pond.n_bluefish,pond.n_redfish,pond.n_carnivorousfish))

    def save(self):
        plt.savefig('figures/fishplot.png',dpi=300)
    
    def saveExit(self,dt):
        plt.savefig('figures/fishplot_{:05d}.png'.format(dt),dpi=300)
        plt.close()