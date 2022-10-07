import sys
import csv
import pandas as pd

'''
    This script takes in command line arguments to combine csv files to create datasets
    The sript can combine as many classes as you would like, and the last argument is 
    The path of the newly generated csv file. The class labels will be replaced
    with an enumeration for the number of csv files being combined.

    The script is ran with the following operation:
    
    python combine_csv.py <path_to_csv1.csv> <path_to_csv2.csv> <path_to_new_csv.csv>
'''

def main(argv):
    with open(argv[-1], 'w') as newCSV:
        filewriter = csv.writer(newCSV, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["image", "class"])
        for class_, file_name in enumerate(argv[1:-1]):
            df = pd.read_csv(file_name)
            images_list = df['image'].tolist()
            for i in images_list:
                filewriter.writerow([i, class_])


if __name__ == '__main__':
    main(sys.argv)