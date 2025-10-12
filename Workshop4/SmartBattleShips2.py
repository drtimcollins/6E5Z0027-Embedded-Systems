import numpy as np
import BattleShips                                 # Import the base BattleShips class

# SmartBattleShips2. Knows not to guess the same cell twice.
# Chooses the first empty cell available.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.argwhere(self.map == ' ')     # Make a list empty cells' coordinates
        return options[0]                          # Select the first of the options
