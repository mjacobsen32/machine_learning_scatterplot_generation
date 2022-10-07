'''
Poly: Polynomial scatter plot
Inherited by: OneDegreePoly
Object attributes:
    y_intercept_range: a range for polynomials to cross the y-intercept
'''
class Poly:
    def __init__(self):
        self.y_intercept_range = (-5, 5)