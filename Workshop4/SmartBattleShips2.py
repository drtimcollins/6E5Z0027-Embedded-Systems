import numpy as np
import BattleShips

# Chooses cells in order.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.array(np.where(self.map == ' ')).T    # Finds coordinates of all untested cells
        return options[0]                                  # Returns coordinates of the first match

b = SmartBattleShips()
b.gui()
