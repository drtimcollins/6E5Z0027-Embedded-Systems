import WordSolver
import random

class SmartSolver(WordSolver.Solver):
   def newGame(self):
      self.wordsRemaining = list(self.wordList)   # Reset the wordsRemaining list each game
      
   def guess(self):
      if len(self.guesses) > 0:
         # Copy all valid members of wordsRemaining (i.e. remove invalid words) 
         self.wordsRemaining = [w for w in self.wordsRemaining if self.isWordValid(w)]
      thisGuess = random.choice(self.wordsRemaining)
      self.wordsRemaining.remove(thisGuess)
      return thisGuess
      
   def isWordValid(self, w):            # Determines if the word, w, is valid
      lastGuess = self.guesses[-1]      # Only need to look at the latest guess
      for i in range(len(w)):           # For each letter in w, check for mismatched '+'s
         if w[i] != lastGuess['word'][i] and lastGuess['response'][i] == '+':
            return False
      return True                       # Return True only if no letters fail the test  
   