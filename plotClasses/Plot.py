'''
Plot: Individual scatterplot variability class and attributes
Inherited by: OneDegreePoly & Grouping
Object attributes:
    sample_range: range of number of samples in given data set
    std_range:  standard deviation range for gaussian distribution variability
                real range is range / 10 for Python random library purposes
    x_range: range of the x value (scatterplots generated without labels and ticks)
    mean: mean for the gaussian distribution variability
'''
class Plot:
    def __init__(self):
        self.sample_range = (15,250)
        self.std_range = (1, 100)
        self.x_low_range = (0,15)
        self.x_high_range = (85,100)
        self.mean = 0
    