import random

class Solver:
    def __init__(self):
        self.guesses = []
        with open('wordList.txt') as f:
            self.wordList = tuple(word.rstrip() for word in f)

    def play(self):
        self.guesses = []
        self.newGame()
        isSolved = False
        numGuesses = 0
        answer = random.choice(self.wordList)
        while not isSolved and numGuesses < 10000:
            g = self.guess()
            numGuesses = numGuesses + 1
            response = ['+' if x == y else '-' for x,y in zip(g, answer)]
            lettersRemaining = [a for a,r in zip(answer,response) if r == '-']
            for i,c in enumerate(g):
                if response[i] == '-' and c in lettersRemaining:
                    response[i] = '*'
                    j = lettersRemaining.index(c)
                    lettersRemaining = lettersRemaining[:j]+lettersRemaining[(j+1):]
            self.guesses.append({'word':g, 'response':''.join(response)})
            isSolved = (g == answer)
        return numGuesses

    def testSolver(self, numGames=100):
        t = 0
        for n in range(numGames):
            t = t + self.play()
        return t / numGames

    def newGame(self):
        pass

    def guess(self):
        return "aaaaaa"
