import random
import numpy as np
import BattleShips

# Very simple guesser. Chooses a random empty cell.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.argwhere(self.map == ' ')     # Make a list of coordinates of empty cells in the map.
        return random.choice(options)              # Choose one of the options at random
