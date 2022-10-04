from Plot import Plot
from sklearn.datasets import make_blobs


'''
Grouping: Grouping scatterplot generation (non polynomials)\
Inherits: Plot 
Object attributes:
    center_box: min and max for generated points to fit into
    n_features: number of features to generate. 2 for (x,y) 2d plot
    centers: number of centers for a grouping (determines stretch and shape)
'''
class Grouping(Plot):
    def __init__(self):
        self.center_box = (-100, 100)
        self.n_features = 2
        self.centers = 1

    def create_plot(self):
       return make_blobs(n_samples=self.sample_range, 
                n_features=self.n_features, 
                centers=1, 
                cluster_std=self.std_range, 
                center_box=(self.center_box))