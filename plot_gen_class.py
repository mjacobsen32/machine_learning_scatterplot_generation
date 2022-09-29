import os
from sqlite3 import Row
from parameters.default_parameters import *
from parameters.constants import *
from plot_functions import *
import matplotlib.pyplot as plt
from sympy import sympify
from sympy import *
import csv

class Plotting:
    def __init__(self):
        self.PARENT_DIR = PARENT_DIR # Path to delete and save new plots
        self.CSV_PARENT_DIR = CSV_PARENT_DIR
        self.CLASS_LABEL = CLASS_LABEL # Class label
        self.CSV_PATH = os.path.join(self.CSV_PARENT_DIR, self.CLASS_LABEL)
        self.PATH = os.path.join(self.PARENT_DIR, self.CLASS_LABEL) # Path to delete and save new plots
        self.CSV_PATH = os.path.join
        self.RGB = RGB                              # Colors to be used in plots by data points
        self.samples_LOW = samples_LOW              # Low range of samples per data set in plot (3 datasets would have min of 60)
        self.samples_HIGH = samples_HIGH            # High range of samples per data set in plot
        self.leading_coe_LOW = leading_coe_LOW      # one degree polynomial low end leading coefficient range 
        self.leading_coe_HIGH = leading_coe_HIGH    # one degree polynomial high end leadig coefficient range
        self.POS_NEG = POS_NEG                      # positive or negative leading coeeficient (1 for positive, -1 for negative)
        self.constant_LOW = constant_LOW            # one degree polynomial low end of constant range
        self.constant_HIGH = constant_HIGH          # one degree polynomial high end of constant range
        self.STD_LOW = STD_LOW                      # standard deviation low end of range for gaussian noise added to data points
        self.STD_HIGH = STD_HIGH                    # standard deviation high end of range for gaussian noise added to data points
        self.DATASETS_PER_PLOT = DATASETS_PER_PLOT  # number of datasets to be plotted on each plot
        self.TOTAL_PLOTS = TOTAL_PLOTS              # total plots to plot and save into PATH with these hyper parameters
        self.POLY = POLY                            # polynomial to scatterplot
        self.Y_INT_LOW = Y_INT_LOW                  # lower end of y intercept
        self.Y_INT_HIGH = Y_INT_HIGH                # upper end of y intercept
        self.delete_tree(REMOVE_TREE)               # removing existing folder

    def delete_tree(self, remove_tree):
        if remove_tree:
            try:
                os.shutil.rmtree(self.PATH)
            except:
                print("Error deleting directory")
            os.mkdir(self.PATH)


    def add_to_csv(self):
        with open(os.path.join(self.CSV_PARENT_DIR, self.CLASS_LABEL)+'.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(["image","label"])
            for i in range(0,self.TOTAL_PLOTS):
                filewriter.writerow([self.CLASS_LABEL+'_'+str(i)+'.png', self.CLASS_LABEL])



    def create_plot(self, i):
        plt.figure(num=0, figsize=(6,6), clear=True)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        plt.axis([0,100,0,100])
        eq = sympify(self.POLY)
        m,x,b = symbols('m x b')
        eq = eq.subs(m,(random.randrange(self.leading_coe_LOW, self.leading_coe_HIGH)/10))
        eq = eq.subs(b,(random.randrange(self.Y_INT_LOW, self.Y_INT_HIGH)/10))
        for j in range(0, self.DATASETS_PER_PLOT):
            (x,y) = scatter(
                func=even_x_equation, 
                eq=eq, 
                n_samples=random.randrange(self.samples_LOW,self.samples_HIGH), 
                mean=0, 
                std=random.randrange(self.STD_LOW,self.STD_HIGH)/10, 
                minx=0, 
                maxx=100)
            plt.scatter(x=x,y=y,c=self.RGB[j])
        plt.savefig(os.path.join(self.PATH,self.CLASS_LABEL+'_'+str(i)+'.png'))

    

#(x,y), labels = scatter(func=blobs, n_samples=100, n_features=2, centers=1,cluster_std=.50,center_box=(-10,10),shuffle=True,random_state=None,return_centers=False)

                
