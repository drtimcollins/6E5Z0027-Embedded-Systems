import BattleShips

# Chooses cells in order.
class SmartBattleShips(BattleShips.BattleShips):
    def newGame(self):
        self.nextGuess = (0,0)                              # Reset next guess at the start of a game

    def guess(self):
        thisGuess = self.nextGuess                          # Copy current nextGuess value
        if thisGuess[1] < self.N - 1:                       # Check for the end of the row...
            self.nextGuess = (thisGuess[0],thisGuess[1]+1)  # ...if not there, then move one cell onwards.
        else:
            self.nextGuess = (thisGuess[0] + 1, 0)          # Row done so start next row and reset column to 0
        return thisGuess

b = SmartBattleShips()
b.gui()
