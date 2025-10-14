## Base BattleShips class: Should be inherited and the guess() method overridden. newGame() method may, optionally, be overridden too
##                         and new methods and/or attributes can be added as needed in the inherited class.
##                         YOU SHOULD NOT NEED TO EDIT THIS FILE IN ANY WAY.

# Numpy package is required and may need to be installed before use.
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

class BattleShips:
    def __init__(self, N = 8):
        if N < 8:
            raise ValueError("Minimum grid size is 8-by-8.")
        self.N = N
        self.map = np.full((self.N, self.N), ' ')
        self.mode = 'auto'
        self.manualGuess = (0,0)

    # Generator function that initialises and plays a complete game (one guess per iteration)
    def playMove(self):
        # On the first iteration, a new game needs to be set up.
        rng = np.random.default_rng(None)
        shipShapes = {'A':((1,1),(1,0)),'B':((2,),(2,),(2,)),'X':((0,3,0),(3,3,3)),'Y':((0,4,0),(4,4,4),(4,0,4))}
        localMap  = np.full((self.N, self.N), 0)        # Stores the solution (only accessible within the generator)
        localHits = np.full((self.N, self.N), 0)
        self.map  = np.full((self.N, self.N), ' ')
        for s in 'YXBA':                                # Place ships (starting with the biggest)
            mask = (convolve(localMap,np.ones((3,3),dtype=int)) == 0)
            validPlacements = []                        # List of all coordinates and rotations where this ship will fit
            for nRotations in range(4):
                sRotated = np.rot90(np.array(shipShapes[s],dtype=int), nRotations)
                xy = np.transpose(np.array(np.where(correlate(mask,sRotated)==np.sum(sRotated)),dtype=int))
                validPlacements = validPlacements + [np.append(c,nRotations) for c in xy]          
            shipPlace = rng.choice(validPlacements)     # Choose one of the valid placement options at random
            localMap = localMap + convolve(np.fromfunction(lambda i,j: (i == shipPlace[0])&(j == shipPlace[1]),
                                (self.N,self.N)).astype(int), np.rot90(np.array(shipShapes[s],dtype=int), shipPlace[2]))
        localMap = np.array([' ','A','B','X','Y'])[localMap]

        self.newGame() 
        numGuesses = 0

        # Iterate through guesses until all fighters are found (this adds up to 16 hits in total) or guesses exceed 1000
        while np.sum(localHits) < 16 and numGuesses < 1000:
            if self.mode == 'auto':
                g = tuple(self.guess())     # Auto mode uses the guess() method to generate guesses
            else:
                g = self.manualGuess        # Manual mode requires a manual guess to be available (used by the gui)
            numGuesses = numGuesses + 1
            if localMap[g] != ' ':          # Cell not empty
                self.map[g] = 'H'           # Mark cell as a hit
                localHits[g] = 1
                # Check for each complete starfighter and mark with the correct code if all cells are hit
                for s in 'ABXY':
                    if np.all(localHits[localMap == s]):
                        self.map[localMap == s] = s
            else:
                self.map[g] = '/'           # Cell was empty so mark as a miss.

            yield self.map.copy()           # Return a copy of the map on each iteration.
    
    # Autoplay - runs a complete game and returns the number of guesses
    def autoplay(self):
        numGuesses = 0
        for _ in self.playMove():
            numGuesses = numGuesses + 1
        return numGuesses
    # Play nGames automatically and return the average number of guesses
    def test(self, nGames=100):
        return np.mean(np.array([self.autoplay() for _ in range(nGames)]))
        
    def newGame(self):
        pass                # Override if any initialisation is needed at the start of a game.    
    
    def guess(self):
        return (0,0)        # Always guesses top-left cell.

    # Launches an interactive graphical user interface to the puzzle. Can be used to play the game manually or test an autosolver
    def gui(self,*,printMap = False):
        self.window = tk.Tk()
        self.window.title("BattleShips")
        self.canv = tk.Canvas(self.window, width=self.N*40, height=self.N*40,borderwidth=0, highlightthickness=0)
        self.btnAuto = ttk.Button(self.window, text="Auto Play", command = self.guiAutoPlay)
        self.btnMan = ttk.Button(self.window, text="Manual Play", command = self.guiManualPlay)
        self.label = tk.Label(self.window, text="")
        self.slider = ttk.Scale(self.window, orient=tk.HORIZONTAL, from_=0, to=1, command = self.sliderChange)
        self.canv.bind('<Any-Button>', self.mouseClick)
        
        self.canv.grid(row=0, column=0, padx=5, pady=5, rowspan=2, columnspan=2)
        self.slider.grid(row=2, column=0, padx=5, pady=5)
        self.btnAuto.grid(row=0, column=2, padx=5, pady=5, sticky='s')
        self.btnMan.grid(row=1, column=2, padx=5, pady=5, sticky='n')
        self.label.grid(row=2,column=1)
        
        self.guiCells = [[self.canv.create_rectangle(x*40,y*40,(x+1)*40-1,(y+1)*40-1,fill='black',outline='green')
                          for x in range(self.N)] for y in range(self.N)]
        self.history = []
        self.printMap = printMap
        self.window.mainloop()
        
    def mouseClick(self, event):
        if self.mode == 'manual':
            if event.num == 1:
                self.manualGuess = (event.y//40,event.x//40)
                try:
                    next(self.manualGame)
                    self.canvasUpdate(self.map)
                    if self.printMap:
                        print(self.map)
                    self.history.append(self.map.copy())
                    self.slider.config(to=len(self.history)-1)
                    self.slider.set(len(self.history)-1)
                except StopIteration:
                    print("Game ended")
            elif event.num == 3:
                r,c = (event.y//40,event.x//40)
                if self.map[r,c] == ' ':
                    self.map[r,c] = '*'
                elif self.map[r,c] == '*':
                    self.map[r,c] = ' '
                if self.printMap:
                    print(self.map)                    
                self.canvasUpdate(self.map)
                
    def sliderChange(self, value):
        if len(self.history) > 0:
            i = int(float(value))
            self.canvasUpdate(self.history[i])
            self.label.config(text=f"Turn {i+1} of {len(self.history)}")
        else:
            self.canvasUpdate(self.map)
            self.label.config(text="")
            
    def guiManualPlay(self):
        self.mode = 'manual'
        self.manualGame = self.playMove()
        self.history = []
        self.map  = np.full((self.N,self.N), ' ')
        self.slider.config(to=len(self.history)-1)
        self.slider.set(0)
        
    def guiAutoPlay(self):   
        self.mode = 'auto'
        self.history = [m for m in self.playMove()]
        if self.printMap:
            for m in self.history:
                print(m)        
        self.slider.config(to=len(self.history)-1)
        self.slider.set(0)
        self.guiCounter = 0
        self.guiPlayAnimate()
        
    def guiPlayAnimate(self):
        self.slider.set(self.guiCounter)
        if self.guiCounter < len(self.history)-1:
            self.guiCounter = self.guiCounter + 1
            self.window.after(50, self.guiPlayAnimate)
            
    def canvasUpdate(self, map):
        colours = {' ':'black','/':'lime green','H':'red','A':'dodger blue','B':'sky blue','X':'gold','Y':'yellow','*':'gray'}
        for r, row in enumerate(self.guiCells):
            for c, cell in enumerate(row):
                self.canv.itemconfig(cell, fill = colours[map[r,c]])

# Two-dimensional convolution between the image array, mp, and the kernel array, mp
def convolve(mp, ker):
    N = np.shape(ker)
    N2 = np.array(N)//2
    M = np.shape(mp)
    c = [np.pad([np.convolve(m, k)[N2[1]:(N2[1]+M[1])] for m in mp],((i,N[0]-1-i),(0,0)),
                'constant',constant_values=0) for i,k in enumerate(ker)]
    if mp.dtype == bool and ker.dtype == bool:
        return np.sum(c,0)[N2[0]:(M[0]+N2[0])] > 0
    else:
        return np.sum(c,0)[N2[0]:(M[0]+N2[0])]


# Two-dimensional correlation between the image array, mp, and the kernel array, mp
def correlate(mp, ker0):
    ker = np.fliplr(ker0)
    N = np.shape(ker)
    N2 = np.array(N)//2
    Nodd = np.array(N) % 2
    M = np.shape(mp)
    c = [np.pad([np.convolve(m, k)[(N2[1]-1+Nodd[1]):(N2[1]+M[1]-1+Nodd[1])] for m in mp], ((N[0]-1-i,i),(0,0)),
                'constant',constant_values=0) for i,k in enumerate(ker)]
    if mp.dtype == bool and ker.dtype == bool:
        return np.sum(c,0)[(N2[0]-1+Nodd[0]):(M[0]+N2[0]-1+Nodd[0])] > 0
    else:
        return np.sum(c,0)[(N2[0]-1+Nodd[0]):(M[0]+N2[0]-1+Nodd[0])]



