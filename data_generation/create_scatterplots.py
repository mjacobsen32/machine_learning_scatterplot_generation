from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import random

PATH = '../data/scatterplots/one_degree/'


def main():
    try:
        shutil.rmtree(PATH)
    except:
        print("Error deleting directory")
    os.mkdir(PATH)

    for i in range(0, 10):
        #(x,y), labels = scatter(func=blobs, n_samples=500, n_features=20, centers=None,cluster_std=.50,center_box=(-10,10),shuffle=True,random_state=None,return_centers=False)
        (x,y), labels = scatter(func=even_x_equation, eq=[2,0], n_samples=100, mean=0, std=3, minx=0, maxx=10)
        plt.scatter(x,y)
        plt.savefig(PATH+'line_'+str(i)+'.png')
        plt.clf()


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