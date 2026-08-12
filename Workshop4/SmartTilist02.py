from itertools import permutations
import numpy as np
from Tilist import Tilist

class TilistPlayer(Tilist):
    def autoPlay(self):
        spaces = np.argwhere(self.grid == '  ')
        
        if self.roundNumber < 3:
            indices = np.random.choice(np.shape(spaces)[0], 4, replace=False)
        else:      
            bestScore = 0
            indices = np.arange(4)

            for trialIndices in permutations(range(np.shape(spaces)[0]), 4):
                testGrid = self.grid.copy()
                
                for i,tile in zip(trialIndices, self.hand):
                    testGrid[tuple(spaces[i])] = tile

                score = self.calculateScores(testGrid)
                
                print(trialIndices, score)
                print(testGrid)
                
                if score > bestScore:
                    bestScore = score
                    indices = np.array(trialIndices)

        print(indices)
        print(type(indices))
        return spaces[indices,:]

mp = TilistPlayer()
mp.gui()
