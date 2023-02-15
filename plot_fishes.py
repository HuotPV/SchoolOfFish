import matplotlib as mpl
import matplotlib.pyplot as plt
import fish

class FishPlot:

    def __init__(self):
        plt.plot([-10,10],[0,0],'k--')
        plt.plot([0,0],[-10,10],'k--')
        self.axes = plt.gca()
        self.axes.set_xlabel('X')
        self.axes.set_xbound(-10,10)
        self.axes.set_ylabel('Y')
        self.axes.set_ybound(-10,10)

    def addFish(self,fish):
        self.axes.plot(fish.pos_x,fish.pos_y,marker=(3, 0, fish.orientation+30))

    def save(self):
        plt.savefig('fishplot.png',dpi=300)
    
