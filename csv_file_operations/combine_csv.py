import sys
import csv
import pandas as pd
import os
from sympy import sympify, sign, simplify, diff

'''
    This script takes in command line arguments to combine csv files to create datasets
    The script can combine as many classes as you would like, and the last argument is 
    The path of the newly generated csv file. The class labels will be replaced
    with an enumeration for the number of csv files being combined.

    The script is ran with the following operation:
    
    python combine_csv.py [<comma separated count from each csv>] <plots from each csv file> <path_to_csv1.csv> <path_to_csv2.csv> <path_to_new_csv.csv>
'''


prefixPath = "/scratch/scatterplots/csv_files"

def one_plot(row):
    eq = diff(sympify(row['equation_0']),'x')
    if eq >= 0:
        return 0
    return 1
    
def two_plot(row):
    eq1 = diff(sympify(row['equation_0']),'x')
    eq2 = diff(sympify(row['equation_1']),'x')
    if eq1 >= 0 and eq2 >= 0:
        return 2
    elif eq1 >= 0 and eq2 < 0:
        return 3
    elif eq1 < 0 and eq2 >= 0:
        return 4
    elif eq1 < 0 and eq2 < 0:
        return 5
    
def three_plot(row):
    eq1 = diff(sympify(row['equation_0']),'x')
    eq2 = diff(sympify(row['equation_1']),'x')
    eq3 = diff(sympify(row['equation_2']),'x')
    if eq1 >=0:
        if eq2 >=0:
            if eq3 >=0:
                return 6
            return 7
        elif eq2 < 0:
            if eq3 >=0:
                return 8
            return 9
    elif eq1 < 0:
        if eq2 >=0:
            if eq3 >=0:
                return 10
            return 11
        elif eq2 < 0:
            if eq3 >=0:
                return 12
            return 13

def get_class(row):
    if 'equation_2' in row:
        return three_plot(row)
    elif 'equation_1' in row:
        return two_plot(row)
    elif 'equation_0' in row:
        return one_plot(row)
    return(row[1])

def main(argv):
    plotsFromEach = argv[1].strip('][').split(',')
    with open(argv[-1], 'w') as newCSV:
        filewriter = csv.writer(newCSV, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["image", "class"])
        for idx, file_name in enumerate(argv[2:-1]):
            df = pd.read_csv(filepath_or_buffer=os.path.join(prefixPath, file_name),
                             nrows=int(plotsFromEach[idx]))
            for row in df.iterrows():
                filewriter.writerow([row[1]['image'], get_class(row[1])])


if __name__ == '__main__':
    main(sys.argv)