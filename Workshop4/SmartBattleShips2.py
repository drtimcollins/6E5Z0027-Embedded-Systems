import random
import numpy as np
import BattleShips

# Very simple guesser. Just chooses random cells regardless of whether they have been tried already.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):
        options = np.array(np.where(self.map == ' ')).T
        return random.choice(options)
        
b = SmartBattleShips()
b.gui()
