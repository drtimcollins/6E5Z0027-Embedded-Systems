import numpy as np
import BattleShips

# Chooses cells in order.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.where(self.map == ' ')                # Finds coordinates of all untested cells
        return (options[0][0],options[1][0])               # Returns coordinates of the first match

b = SmartBattleShips()
b.gui()
