from plot_gen_class import Plotting
from OneDegreePoly import OneDegreePoly
from Grouping import Grouping

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
    p = Plotting('triple_threat', 10, True)

    strong_pos = OneDegreePoly()

    strong_neg = OneDegreePoly()
    strong_neg.pos_neg = -1

    weak_pos = OneDegreePoly()
    weak_pos.std_range = (100,300)

    p.plots = [strong_pos, strong_neg, weak_pos]
    loop_create(p)
    p.add_to_csv()


if __name__ == "__main__":
    main()