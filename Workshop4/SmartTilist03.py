from itertools import permutations
import numpy as np
from Tilist import Tilist

class TilistPlayer(Tilist):
    def autoPlay(self):
        spaces = np.argwhere(self.grid == '  ')    # Make list of available spaces
 
        # Initialise the best score found so far to -1
        bestScore = -1
        indices = np.arange(4)

        if self.roundNumber < 3:                   # For rounds 0-2, choose at random
            for trial in range(12):                # Try 12 random permutations
                trialIndices = np.random.choice(np.shape(spaces)[0], 4, replace=False)
                testGrid = self.grid.copy()                  # Copy current grid so we can
                                                             # try out this permutation.
                for i,tile in zip(trialIndices, self.hand):  # Place each tile in the hand
                    testGrid[tuple(spaces[i])] = tile        # into the testGrid.

                score = self.calculateScores(testGrid)       # Score this test placement
                                
                if score > bestScore:                        # If it beats the best so far
                    bestScore = score                        # then set this score as the
                    indices = np.array(trialIndices)         # new best and store indices.
        else:
            # Iterate through every permutation of possible placements 
            for trialIndices in permutations(range(np.shape(spaces)[0])):
                testGrid = self.grid.copy()                  # Copy current grid so we can
                                                             # try out this permutation.
                for i,tile in zip(trialIndices, self.hand):  # Place each tile in the hand
                    testGrid[tuple(spaces[i])] = tile        # into the testGrid.

                score = self.calculateScores(testGrid)       # Score this test placement
                                
                if score > bestScore:                        # If it beats the best so far
                    bestScore = score                        # then set this score as the
                    indices = np.array(trialIndices)         # new best and store indices.

        return spaces[indices]                               # Return coordinates as before
      