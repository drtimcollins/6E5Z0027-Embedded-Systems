import random
import numpy as np
import BattleShips                                 # Import the base BattleShips class

# SmartBattleShips3. Knows not to guess the same cell twice.
# Chooses a cell at random from a list of all empty cells.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.argwhere(self.map == ' ')     # Make a list empty cells' coordinates
        return random.choice(options)              # Choose one of the options at random
