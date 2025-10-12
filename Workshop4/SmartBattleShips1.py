import random
import BattleShips                              # Import the base BattleShips class

# SmartBattleShips1. Very simple guesser.
# Just chooses random cells regardless of whether they have been tried already.
class SmartBattleShips(BattleShips.BattleShips):
    def guess(self):                            # Override the base guess() method
        return (random.randint(0,self.N-1), random.randint(0,self.N-1))
