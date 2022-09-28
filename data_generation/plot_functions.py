import numpy as np
from sklearn.datasets import make_blobs
import random
from sympy import *

def scatter(func, **kwargs):
        points = func(**kwargs)
        points = np.array(points)
        return (points[:,0], points[:,1])

def even_x_equation(eq, n_samples, mean, std, minx, maxx):
    Xs = np.linspace(minx, maxx, n_samples)
    x = symbols('x')
    Y = np.array([eq.subs(x,X) + random.gauss(mean,std) for X in Xs])
    return (np.stack((Xs,Y), axis=-1))



def blobs(**kwargs):
    return make_blobs(**kwargs)