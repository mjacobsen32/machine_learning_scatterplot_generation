import os
from parameters.constants import *
import matplotlib.pyplot as plt
import csv

'''
Plotting: Plotting class for all plotting generating operations
Object attributes:
    parent_dir: parent dir for images, can be changed for different classification problems
    csv_parent_dir: csv parent directory, can be changed for different classification problems
    class_label: class label to be used for directory, csv labels, and images
    images_path: path to create and save all png plots
    csv_path: path to create and save the csv file
    rgb: color scheme to use for points in the plot
    total_plots: total number of png plots to generate
    plots: list of Plot objects to create in each png plot
    delete_tree: bool to delete images directory
'''

class Plotting:
    def __init__(self, label, total, remove_tree):
        self.parent_dir = parent_dir
        self.csv_parent_dir = csv_parent_dir
        self.class_label = label
        self.images_path = os.path.join(self.parent_dir, self.class_label)
        self.csv_path = os.path.join(self.csv_parent_dir, self.class_label)
        self.rgb = rgb
        self.total_plots = total
        self.plots = []
        self.delete_tree(remove_tree)
        self.equations = []
        self.samples = []
        self.std = []

    def delete_tree(self, remove_tree):
        if os.path.exists(self.images_path):
            if remove_tree:
                try:
                    os.shutil.rmtree(self.images_path, ignore_errors=True)
                except:
                    print("Error deleting directory: {}".format(self.images_path))
        else:
            os.mkdir(self.images_path)

    def add_to_csv(self):
        with open(self.csv_path+'.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["image","label","equation1","samples1","std1",
            "equation2","samples2","std2",
            "equation3","samples3","std3"])
            for i in range(0, self.total_plots):
                filewriter.writerow([self.class_label+'_'+str(i)+'.png', 
                                        self.class_label,
                                        self.equations[i][0],
                                        self.samples[i][0],
                                        self.std[i][0],
                                        None if len(self.equations[i]) < 2 else self.equations[i][1],
                                        None if len(self.samples[i]) < 2 else self.samples[i][1],
                                        None if len(self.std[i]) < 2 else self.std[i][1],
                                        None if len(self.equations[i]) < 3 else self.equations[i][2],
                                        None if len(self.samples[i]) < 3 else self.samples[i][2],
                                        None if len(self.std[i]) < 3 else self.std[i][2]])



    def create_plot(self, i):
        plt.figure(num=0, figsize=(6,6), clear=True)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.axis([0,100,0,100])
        equationsPlot = []
        stdPlot = []
        samplesPlot = []
        for j, p in enumerate(self.plots):
            x, y, eq, sample, std = p.gen_plot()
            equationsPlot.append(eq)
            stdPlot.append(std)
            samplesPlot.append(sample)
            plt.scatter(x=x,y=y,c=self.rgb[j])
        self.samples.append(samplesPlot)
        self.std.append(stdPlot)
        self.equations.append(equationsPlot)
        plt.savefig(os.path.join(self.images_path,self.class_label+'_'+str(i)+'.png'))
        

                
