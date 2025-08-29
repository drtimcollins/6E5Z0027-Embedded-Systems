import random
import BattleShips

# Very simple guesser. Just chooses random cells regardless of whether they have been tried already.
class SmartBattleShips(BattleShips.BattleShips):
	def guess(self):
		return (random.randint(0,self.N-1), random.randint(0,self.N-1))

b = SmartBattleShips()
b.gui()
