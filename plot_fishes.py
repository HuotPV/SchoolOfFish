import matplotlib as mpl
import matplotlib.pyplot as plt
import fish
from matplotlib.markers import MarkerStyle

class FishPlot:

    def __init__(self):
        plt.plot([-100,100],[0,0],'k--')
        plt.plot([0,0],[-100,100],'k--')
        self.axes = plt.gca()
        self.axes.set_xlabel('X')
        self.axes.set_xbound(-100,100)
        self.axes.set_ylabel('Y')
        self.axes.set_ybound(-100,100)

    def addFish(self,fish):
        m = MarkerStyle("^")
        m._transform.scale(0.7, 1)
        m._transform.rotate_deg(fish.orientation-90)
        self.axes.plot(fish.pos_x,fish.pos_y,marker=m, markeredgecolor = [0.1,0.1,0.1],linewidth=1, markerfacecolor = fish.color, markersize=5)

    def save(self):
        plt.savefig('fishplot.png',dpi=300)
    
