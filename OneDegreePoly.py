from Plot import Plot
from Poly import Poly
from sympy import sympify, symbols
import random
import numpy as np

class OneDegreePoly(Plot, Poly):
    def __init__(self):
        Poly.__init__(self)
        Plot.__init__(self)
        self.lead_coe_range = (1, 30)  # leading coefficient range for line creation
        self.pos_neg        = 1            # positive or negative leading coeeficient (1 for positive, -1 for negative, 0 for both)
        self.equation       = "(m*x) + b"  # equation to scatterplot

    def gen_plot(self):
        eq = sympify(self.equation)
        m, x, b = symbols('m x b')
        eq = eq.subs(m, self.pos_neg * random.randrange(*self.lead_coe_range)/10)
        eq = eq.subs(b, 100 - (self.pos_neg* random.randrange(*self.y_intercept_range)))
        samples = random.randrange(*self.sample_range)
        std = random.randrange(*self.std_range)/10
        X_list = np.linspace(*self.x_range, samples)
        Y_list = np.array([eq.subs(x,X) + random.gauss(self.mean, std) for X in X_list])
        return (X_list, Y_list)
