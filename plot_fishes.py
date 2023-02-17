import matplotlib as mpl
import matplotlib.pyplot as plt
import fish
from matplotlib.markers import MarkerStyle

class FishPlot:

    def __init__(self):
        #plt.plot([-145,145],[0,0],'k--')
        #plt.plot([0,0],[-145,145],'k--')
        self.axes = plt.gca()
        self.axes.set_xlabel('X')
        self.axes.set_xbound(-225,225)
        self.axes.set_ylabel('Y')
        self.axes.set_ybound(-225,225)

    def addFish(self,fish):
        m = MarkerStyle("^")
        m._transform.scale(0.7, 1)
        m._transform.rotate_deg(fish.orientation-90)
        self.axes.plot(fish.pos_x,fish.pos_y,marker=m, markeredgecolor = [0.1,0.1,0.1],linewidth=1, markerfacecolor = fish.color, markersize=5)
        self.axes.set_ybound(-225,225)
        self.axes.set_xbound(-225,225)

    def addZones(self,fish):
        circle1 = plt.Circle((fish.pos_x, fish.pos_y), fish.aim_radius, color=fish.color, alpha=0.1)
        circle2 = plt.Circle((fish.pos_x, fish.pos_y), fish.imitate_radius, color=fish.color, alpha=0.5)
        circle3 = plt.Circle((fish.pos_x, fish.pos_y), fish.repel_radius, color=fish.color, alpha=0.8)
        self.axes.add_patch(circle1)
        self.axes.add_patch(circle2)
        self.axes.add_patch(circle3)

    def save(self):
        plt.savefig('figures/fishplot.png',dpi=300)
    
    def saveExit(self,dt):
        plt.savefig('figures/fishplot_{:05d}.png'.format(dt),dpi=300)
        plt.close()