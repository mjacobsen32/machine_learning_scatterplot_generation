from plotClasses.PlotGen import Plotting
from plotClasses.OneDegreePoly import OneDegreePoly
from plotClasses.Grouping import Grouping
from parameters.constants import *

'''
    Notes:
        Defined correlations for this study:
            Strong Correlation: Standard deviation  = < 3.0
            Weak Correlation:   Standard deviation  = > 3.0 && < 10.0
            No Correlation:     Standard deviation  = > 5.0
                                Leading coefficient = < 0.1
        
        CSV files are generated with each run of this program such that there is
        a new CSV file in every generated folder. Each CSV file in theory would
        contain the same class, so that when creating the classification problem
        you can simply combine desired folders images and csv files to generate 
        the desired data set for training. 
        The class designated for the CSV file, folder name, and png name can be 
        declared using the above "CLASS_LABEL"
'''

def loop_create(p):
    for i in range(0, p.total_plots):
        if (i != 0) and (i % 100 == 0):
            print(i)
        p.create_plot(i)

def main():    
    p6 = Plotting(label='sixLines', total=1000, remove_tree=False, color_scheme=purples)
    p5 = Plotting(label='fiveLines', total=1000, remove_tree=False, color_scheme=purples)
    p4 = Plotting(label='fourLines', total=1000, remove_tree=False, color_scheme=purples)
    p3 = Plotting(label='threeLines', total=1000, remove_tree=False, color_scheme=purples)
    p2 = Plotting(label='twoLines', total=1000, remove_tree=False, color_scheme=purples)
    p1 = Plotting(label='oneLines', total=1000, remove_tree=False, color_scheme=purples)

    toCreate = [p1,p2,p3,p4,p5,p6]
    randomOneDegree = OneDegreePoly()

    for tot, p in enumerate(toCreate):
        p.plots = [randomOneDegree for _ in range(tot+1)]
        loop_create(p)
        p.add_to_csv()

if __name__ == "__main__":
    main()