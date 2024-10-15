import random

class Solver:
    def __init__(self):
        self.guesses = []                                       # A list of all guesses made so far with results
        with open('wordList.txt') as f:
            self.wordList = tuple(word.rstrip() for word in f)  # The complete list of possible words.

    def play(self):                                             # Plays a single game - this method should NOT be overridden
        self.guesses = []                                       # Reset guesses list to nothing
        self.newGame()                                          # Any additional initialisation can go in the newGame() method
        isSolved = False
        numGuesses = 0
        answer = random.choice(self.wordList)                   # Choose a word at random from the list
        while not isSolved and numGuesses < 10000:              # Loop until solved or the 10000 guess limit is reached
            g = self.guess()                                    # The guess() method will need overriding in inherited SmartSolvers
            numGuesses = numGuesses + 1
            response = ['+' if x == y else '-' for x,y in zip(g, answer)]           # Check each letter for '+' result
            lettersRemaining = [a for a,r in zip(answer,response) if r == '-']      # All letters not already graded '+'
            for i,c in enumerate(g):
                if response[i] == '-' and c in lettersRemaining:                    # If a letter is in the word but elsewhere...
                    response[i] = '*'                                               # ...response = '*'
                    j = lettersRemaining.index(c)
                    lettersRemaining = lettersRemaining[:j]+lettersRemaining[(j+1):]    # Once found, remove from list in case of duplicates
            self.guesses.append({'word':g, 'response':''.join(response)})
            isSolved = (g == answer)
        return numGuesses

    def testSolver(self, numGames=100):
        t = 0
        for n in range(numGames):
            t = t + self.play()
        return t / numGames

    def newGame(self):
        pass                # Override if any initialisation is needed at the start of a game.

    def guess(self):
        return "aaaaaa"     # SmartSolvers will override this to give better guesses.
