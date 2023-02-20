import csv
import pathlib
import os

class Outfile:

    def __init__(self,fishs):
        self.path = os.getcwd() + "/outputs"
        self.name = 'fishs_status'
        self.ext = '.csv'
        self.file_name = self.path  + '/' + self.name + self.ext
        self.fishes = fishs
        self.header = ['id','type','step','status','x','y','u','v','dir','groupsize']

        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

        with open(self.path  + '/' + self.name + self.ext,  'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(self.header)


    def addFish(self,fishs,tstep):
        with open(self.path + '/' +  self.name + self.ext, 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)


            for fish in fishs:
                if fish.isalive == 1:
                    line = [fish.id, fish.type, fish.isalive, tstep, '{:.2f}'.format(fish.pos_x), '{:.2f}'.format(fish.pos_y), 
                        '{:.2f}'.format(fish.velocity[0]), '{:.2f}'.format(fish.velocity[1]), 
                        '{:.2f}'.format(fish.orientation), fish.number_in_group ]
                else:
                    line = [fish.id, fish.type, fish.isalive, tstep, '', '', '', '', '' , '' ]

                writer.writerow(line)

