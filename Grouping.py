from Plot import Plot
from sklearn.datasets import make_blobs

class Grouping(Plot):
    def __init__(self):
        self.center_box = (-100, 100)
        self.n_features = 2
        self.centers = 1

    def create_plot(self):
        print('here')
        #make_blobs()