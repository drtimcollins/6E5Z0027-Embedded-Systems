import WordSolver
import random

class SmartSolver(WordSolver.Solver):
   def newGame(self):                                  # Called at the start of each 'play'
      self.wordsRemaining = list(self.wordList)        # Make a list copy of wordList
      
   def guess(self):
      thisGuess = random.choice(self.wordsRemaining)   # Select a word at random...
      self.wordsRemaining.remove(thisGuess)            # ...and remove it from the list
      return thisGuess
