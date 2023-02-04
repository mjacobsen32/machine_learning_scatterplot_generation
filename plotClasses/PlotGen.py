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
    def __init__(self, label, total, remove_tree, color_scheme=rgb):
        self.parent_dir = parent_dir
        self.csv_parent_dir = csv_parent_dir
        self.class_label = label
        self.images_path = os.path.join(self.parent_dir, self.class_label)
        self.csv_path = os.path.join(self.csv_parent_dir, self.class_label)
        self.rgb = color_scheme
        self.total_plots = total
        self.plots = []
        self.delete_tree(remove_tree)
        self.equations = []
        self.samples = []
        self.std = []

    def delete_tree(self, remove_tree):
        #if os.path.exists(self.images_path):
        #    if remove_tree:
        #        try:
        #            os.shutil.rmtree(self.images_path, ignore_errors=True)
        #        except:
        #            print("Error deleting directory: {}".format(self.images_path))
        #else:
        #os.mkdir(self.images_path)
        return

    def add_to_csv(self):
        with open(self.csv_path+'.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            topRow = ["image", "label"]

            for i in range(len(self.plots)):
                topRow += ["equation_"+str(i),"samples_"+str(i),"std_"+str(i)] 

            filewriter.writerow(topRow)
            for i in range(0, self.total_plots):
                row = [self.class_label+'_'+str(i)+'.png',self.class_label]
                for j in range(len(self.plots)):
                    row+= [str(self.equations[i][j]), str(self.samples[i][j]), str(self.std[i][j])]
                filewriter.writerow(row)



    def create_plot(self, i):
        plt.figure(num=0, figsize=(6,6), clear=True, facecolor=(0.0, 0.0, 0.0))
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.axis([0,100,0,100])
        #plt.Axes.set_facecolor(color=(0.0, 0.0, 0.0))
        equationsPlot = []
        stdPlot = []
        samplesPlot = []
        for j, p in enumerate(self.plots):
            x, y, eq, sample, std = p.gen_plot()
            equationsPlot.append(eq)
            stdPlot.append(std)
            samplesPlot.append(sample)
            plt.scatter(x=x,y=y,color=self.rgb[j], edgecolors='face')
        plt.gca().set(facecolor=(0.0, 0.0, 0.0))
        #plt.margins(x=0, y=0)
        plt.tight_layout()
        self.samples.append(samplesPlot)
        self.std.append(stdPlot)
        self.equations.append(equationsPlot)
        plt.savefig(os.path.join(self.images_path,self.class_label+'_'+str(i)+'.png'))
        

                
