from tkinter.tix import Tree
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import random

PATH = '../data/scatterplots/one_degree/'
RGB = ['blue', 'red', 'green']
samples_LOW = 20
samples_HIGH = 250
one_degree_LOW = 1
one_degree_HIGH = 60
one_degree_b_LOW = 0
one_degree_b_HIGH = 800
STD_LOW = 1
STD_HIGH = 100
#(x,y), labels = scatter(func=blobs, n_samples=100, n_features=2, centers=1,cluster_std=.50,center_box=(-10,10),shuffle=True,random_state=None,return_centers=False)

def main():
    try:
        shutil.rmtree(PATH)
    except:
        print("Error deleting directory")
    os.mkdir(PATH)

    for i in range(0, 10):
        s = plt.figure(figsize=(6,6), clear=True)
        plt.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)
        (x,y), labels = scatter(
            func=even_x_equation, 
            eq=[(-1*random.randrange(one_degree_LOW,one_degree_HIGH)/10),(random.randrange(one_degree_b_LOW,one_degree_b_HIGH)/10)], 
            n_samples=random.randrange(samples_LOW,samples_HIGH), 
            mean=0, 
            std=random.randrange(STD_LOW,STD_HIGH), 
            minx=0, 
            maxx=100)
        plt.scatter(x=x,y=y,c='Red')
        (x,y), labels = scatter(
            func=even_x_equation, 
            eq=[(random.randrange(one_degree_LOW,one_degree_HIGH)/10),(random.randrange(one_degree_b_LOW,one_degree_b_HIGH)/10)], 
            n_samples=random.randrange(samples_LOW,samples_HIGH), 
            mean=0, 
            std=random.randrange(STD_LOW,STD_HIGH), 
            minx=0, 
            maxx=100)
        plt.scatter(x=x,y=y,c='Green')

        s.savefig(PATH+'line_'+str(i)+'.png', )
        s.clear()


def scatter(func, **kwargs):
    points, labels = func(**kwargs)
    points = np.array(points)
    return (points[:,0], points[:,1]), labels

def equate(poly, x):
    n = len(poly)
    result = 0
    for i in range(0,n):
        Sum = poly[i]
        for j in range(n - i - 1):
            Sum = Sum * x
        result = result + Sum
    return result


def even_x_equation(eq, n_samples, mean, std, minx, maxx):
    X = np.linspace(minx, maxx, n_samples)
    Y = np.array([equate(eq,x) + random.gauss(mean,std) for x in X])
    return (np.stack((X,Y), axis=-1)), 1



def blobs(**kwargs):
    return make_blobs(**kwargs)


if __name__ == "__main__":
    main()