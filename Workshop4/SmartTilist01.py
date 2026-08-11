import numpy as np
from Tilist import Tilist

class TilistPlayer(Tilist):
    def autoPlay(self):
        spaces = np.argwhere(self.grid=='  ')                       # List of coordinates of unfilled grid spaces
        i = np.random.choice(np.shape(spaces)[0], 4, replace=False) # Choose 4 random, unique, row indices from spaces
        return spaces[i]                                            # and return those rows
