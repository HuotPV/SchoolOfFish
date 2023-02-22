import pandas as pd
import seaborn as sns
import matplotlib as plt
from pond import Pond
import pathlib
import os

class Analysis:

    def __init__(self,path,pond):
        self.path = os.getcwd() + "/diags"
        self.data = pd.read_csv(path)
        self.border = pond.border
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)


    def plot_fish_direction_distr(self):
        
        #dir_subset = [col for col in self.data if col.endswith('direction')]
    
        dist_plot = sns.displot(data=self.data, x="dir", hue="type", stat="density", common_norm=False) # kind = "kde" to have lines instead of bars
                                                                                                        # but normalization stops working ...

        fig = dist_plot.fig
        fig.savefig(self.path+"/out_dir.png",dpi=300) 


    def plot_fish_groupsize_distr(self):
        
        grpsize_subset = self.data.loc[(self.data["type"] == "BlueFish") | (self.data["type"] == "RedFish")]

        #dist_plot = sns.displot(data=grpsize_subset, x="groupsize", hue="type", stat="density", common_norm=False)
        dist_plot = sns.histplot(data=grpsize_subset, x="groupsize", hue="type",binwidth=1)

        fig = dist_plot.get_figure()
        fig.savefig(self.path+"/out_grpsize.png",dpi=300) 

    def plot_fish_location_pdf(self,type,border):
        
        grpsize_subset = self.data.loc[(self.data["type"] == type)]

        #dist_plot = sns.displot(data=grpsize_subset, x="groupsize", hue="type", stat="density", common_norm=False)
        dis_plot = sns.displot(grpsize_subset, x="x", y="y", binwidth=(10, 10), cbar=True)
        dis_plot.set(ylim=(-1.5*border, 1.5*border))
        dis_plot.set(xlim=(-1.5*border, 1.5*border))
        fig = dis_plot.fig
        fig.savefig(self.path+"/out_location_pdf_"+type+".png",dpi=300) 

    def analysis_set(self):
        self.plot_fish_groupsize_distr()
        self.plot_fish_direction_distr()
        self.plot_fish_location_pdf("BlueFish",self.border)
        self.plot_fish_location_pdf("RedFish",self.border)
        self.plot_fish_location_pdf("CarnivorousFish",self.border)

if __name__ == "__main__":
    pond = Pond(0,0,0)
    my_diag = Analysis('/home/pv/Documents/code/python/SchoolOfFish/outputs/fishs_status.csv',pond)
    my_diag.plot_fish_groupsize_distr()
    my_diag.plot_fish_direction_distr()
    my_diag.plot_fish_location_pdf("BlueFish",my_diag.border)
    my_diag.plot_fish_location_pdf("RedFish",my_diag.border)
    my_diag.plot_fish_location_pdf("CarnivorousFish",my_diag.border)
