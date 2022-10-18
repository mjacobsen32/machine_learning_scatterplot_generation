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
    p6 = Plotting(label='6_lines', total=10, remove_tree=False, color_scheme=purples)
    
    randomOneDegree = OneDegreePoly()

    p6.plots = [randomOneDegree, randomOneDegree, randomOneDegree, randomOneDegree, randomOneDegree, randomOneDegree]
    loop_create(p6)
    p6.add_to_csv()

if __name__ == "__main__":
    main()