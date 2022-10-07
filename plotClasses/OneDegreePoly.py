from turtle import setpos
from .Plot import Plot
from .Poly import Poly
from sympy import sympify, symbols
import random
import numpy as np

'''
OneDegreePoly: One degree polynomial creation
Inherits: Plot for variability attributes, and Poly for y-intercept and 
            other future Polynomial specific attributes
Object attributes:
    lead_coe_rang: leading coefficient range (divided by 10 for python library sake)
    pos_neg: positive or negative leading coefficient
    equation: equation for all one degree polynomials to use
'''

class OneDegreePoly(Plot, Poly):
    def __init__(self, lead_coe_range=(0, 40), pos_neg=0):
        Poly.__init__(self)
        Plot.__init__(self)
        self.lead_coe_range = lead_coe_range
        self.pos_neg        = pos_neg
        self.lead           = random.choice([-1,1]) if self.pos_neg == 0 else self.pos_neg
        self.equation       = "(m*x) + b"

    def get_b(self):
        r = random.randrange(*self.y_intercept_range)
        if self.lead == 1:
            return r
        elif self.lead == -1:
            return 100 -r

    def newLead(self):
        self.lead = random.choice([-1,1]) if self.pos_neg == 0 else self.pos_neg

    def gen_plot(self):
        if self.pos_neg == 0: self.newLead()
        eq = sympify(self.equation)
        m, x, b = symbols('m x b')
        eq = eq.subs(m, self.lead  * random.randrange(*self.lead_coe_range)/10)
        eq = eq.subs(b, self.get_b())
        samples = random.randrange(*self.sample_range)
        std = random.randrange(*self.std_range)/10
        X_list = np.linspace(random.randrange(*self.x_low_range), random.randrange(*self.x_high_range), samples)
        Y_list = np.array([eq.subs(x,X) + random.gauss(self.mean, std) for X in X_list])
        return X_list, Y_list, eq, samples, std
