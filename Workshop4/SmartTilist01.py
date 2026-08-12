import numpy as np
from Tilist import Tilist

class TilistPlayer(Tilist):
    def autoPlay(self):
        # Make an array that is a list of coordinates of available grid spaces
        spaces = np.argwhere(self.grid == '  ')
        # Choose 4 random, unique, numbers from 0 to the no. of spaces - 1
        indices = np.random.choice(np.shape(spaces)[0], 4, replace=False)
        # Return the randomly selected rows from the spaces list
        return spaces[indices]
