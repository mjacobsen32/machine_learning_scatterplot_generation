from codecs import ignore_errors
import os
from parameters.constants import *
import matplotlib.pyplot as plt
import csv

class Plotting:
    def __init__(self, label, total, remove_tree):
        self.parent_dir = parent_dir # Path to delete and save new image folders
        self.csv_parent_dir = csv_parent_dir # Path to save and delete new CSV files
        self.class_label = label # class labels
        self.images_path = os.path.join(self.parent_dir, self.class_label)
        self.csv_path = os.path.join(self.csv_parent_dir, self.class_label)
        self.rgb = rgb                              # Colors to be used in plots by data points
        self.total_plots = total              # total plots to plot and save into path with these hyper parameters
        self.plots = []
        self.delete_tree(remove_tree)               # removing existing folder

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
        

                
