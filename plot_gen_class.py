from codecs import ignore_errors
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

    def delete_tree(self, remove_tree):
        if os.path.exists(self.images_path):
            if remove_tree:
                try:
                    os.shutil.rmtree(self.images_path, ignore_errors=True)
                    os.mkdir(self.images_path)
                except:
                    print("Error deleting directory: {}".format(self.images_path))


    def add_to_csv(self):
        with open(self.csv_path+'.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["image","label"])
            for i in range(0,self.total_plots):
                filewriter.writerow([self.class_label+'_'+str(i)+'.png', self.class_label])



    def create_plot(self, i):
        plt.figure(num=0, figsize=(6,6), clear=True)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.axis([0,100,0,100])
        for j, p in enumerate(self.plots):
            (x,y) = p.gen_plot()
            plt.scatter(x=x,y=y,c=self.rgb[j])
        plt.savefig(os.path.join(self.images_path,self.class_label+'_'+str(i)+'.png'))
        

                
