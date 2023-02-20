import csv
import pathlib
import os


class Outfile:

    def __init__(self,fishs):
        self.path = os.getcwd() + "/outputs"
        self.name = 'fishs_status'
        self.ext = '.csv'
        self.fishes = fishs
        self.header = []

        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

        for fish in self.fishes:
            self.header = self.header + ['Step','Id {}'.format(fish.id),'Fish {} status'.format(fish.id), 'Fish {} x pos.'.format(fish.id),'Fish {} y pos.'.format(fish.id)]
            self.header = self.header +['Fish {} x vel.'.format(fish.id),'Fish {} y vel.'.format(fish.id),'Fish {} orientation.'.format(fish.id)]

        with open(self.path  + '/' + self.name + self.ext, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(self.header)

    def addFish(self,fishs,tstep):
        with open(self.path + '/' +  self.name + self.ext, 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)

            line = []

            for fish in fishs:
                line = line + [tstep,fish.id, fish.isalive, '{:.2f}'.format(fish.pos_x), '{:.2f}'.format(fish.pos_y)]
                line = line + ['{:.2f}'.format(fish.velocity[0]), '{:.2f}'.format(fish.velocity[1]), '{:.2f}'.format(fish.orientation)]

            writer.writerow(line)
