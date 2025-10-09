import numpy as np
import BattleShips

# Very simple guesser. Chooses first empty cell available.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.argwhere(self.map == ' ')     # Make a list of coordinates of empty cells in the map.
        return options[0]                          # Select the first of the options
