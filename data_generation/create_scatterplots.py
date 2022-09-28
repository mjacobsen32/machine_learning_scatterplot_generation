from plot_gen_class import Plotting


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
    for i in range(0, p.TOTAL_PLOTS):
        if (i % 100 == 0):
            print(i)
        p.create_plot(i)

def main():    
    p = Plotting()

    #p.CLASS_LABEL = "one_strong_pos"
    #loop_create(p)
    #p.add_to_csv()

    #p.POS_NEG = -1
    #p.CLASS_LABEL = "one_strong_neg"
    #loop_create(p)
    #p.add_to_csv()

    p.TOTAL_PLOTS = 10
    p.STD_HIGH = 1000
    p.STD_LOW = 100
    p.POS_NEG = 1
    p.CLASS_LABEL = "one_weak_pos"
    loop_create(p)
    p.add_to_csv()

    p.POS_NEG = -1
    p.CLASS_LABEL = "one_weak_neg"
    loop_create(p)
    p.add_to_csv()

    p.leading_coe_HIGH = 0
    p.leading_coe_LOW = 0
    p.STD_LOW = 500
    p.POS_NEG = 1
    p.CLASS_LABEL = "one_no_correlation"
    loop_create(p)
    p.add_to_csv()

if __name__ == "__main__":
    main()