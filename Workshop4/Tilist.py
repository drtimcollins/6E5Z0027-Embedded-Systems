## Base Tilist class: Should be inherited and the autoPlay() method overridden and
##                    new methods and/or attributes can be added as needed in the inherited class.
##                    YOU SHOULD NOT NEED TO EDIT THIS FILE IN ANY WAY.

# Numpy package is required and may need to be installed before use.
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
cols = {'R':'red4','B':'blue','G':'dark green'}
tileBag = np.array([c+str(n) for c in 'RBG' for n in range(1,10)])
scoreLabels = [f'{rc} {n}' for rc in ['Row','Column'] for n in range(4)]
icons = {'R': np.array([[0,0],[0,32],[32,32],[32,0]]) - 16, 
         'B':np.array([[16,0],[32,16],[16,32],[0,16]]) - 16,
         'G':np.array([[0,16],[8,2],[24,2],[32,16],[24,30],[8,30]]) - 16, 
         '-':np.array([[-16,-16],[16,-16]])}
iconCol = {'R':'red2','G':'green4','B':'RoyalBlue3','-':'azure4'}
class Tilist:
    def __init__(self):
        self.initGameData()

    def autoPlay(self):   # Base version always plays tiles in consecutive rows.
        return [(self.roundNumber, i) for i in range(4)]        
 
    def playGame(self):
        for score in self.playTurn():
            if self.roundNumber < 4:
                self.playLocations = self.autoPlay()
        return score
    
    def playGames(self, N=10):
        return float(np.mean(np.array([self.playGame() for _ in range(N)])))
 
    def initGameData(self):
        self.grid = np.full((4, 4), '  ')
        self.hand = np.full(4, '  ')
        self.gameOver = False
        self.roundNumber = 0
        
    # Generator function that initialises and plays a complete game (one guess per iteration)
    def playTurn(self):
        self.initGameData()
        # Randomly selects 20 tiles from the bag
        deal = np.random.choice(tileBag, 16, replace=False)
       
        currentScore = 0
        for i in range(5):
            self.roundNumber = i
            if i > 0:
                # Copy tiles into grid and discard
                for i,p in enumerate(self.playLocations):
                    self.grid[tuple(p)] = self.hand[i]

                currentScore = self.calculateScores()
            
            self.hand = deal[:4]
            deal = deal[4:]                
            
            if i == 4:
                self.gameOver = True            

            yield currentScore
    
    def calculateScores(self, grid=None):
        if grid is None:
            scores = [self.getScore(i, self.grid) for i in range(8)]
            self.scores = scores
        else:
            scores = [self.getScore(i, grid) for i in range(8)]            
        return sum([s['score'] for s in scores])

    def getScore(self, index, grid):
        if index < 4:
            comb = grid[index,:]
        else:
            comb = grid[:,index-4]
        nums = np.array([int(x[1]) if x!='  ' else -1 for x in comb])
        clrs = np.array([x[0] if x!='  ' else '' for x in comb])
        if np.sum(nums > 0):
            nu,nc = np.unique(nums[nums > 0], return_counts=True)
            _,cc = np.unique(clrs[clrs != ''], return_counts=True)
            allSameColour = (cc[0] == 4)
            sameNumbers = np.max(nc)
            twoPair = np.all(nc == 2) and (len(nc) == 2)
            isRun = (len(nc) == 4) and (np.min(nu) == np.max(nu)-3)
            if isRun and allSameColour: return {'score':10, 'label':'Run Same Colour'}
            if isRun: return {'score':6, 'label':'Run of 4'}
            if sameNumbers == 3: return {'score':4, 'label':'3 Same Number'}
            if allSameColour: return {'score':3, 'label':'All Same Colour'}
            if twoPair: return {'score':2, 'label':'Two Pairs'}
        return {'score':0, 'label':''}

    def gui(self):
        self.currentGame = self.playTurn()
        next(self.currentGame)
        
        self.window = tk.Tk()
        self.window.title('Tilist')        
        self.window.iconphoto(False, tk.PhotoImage(master=self.window, data="R0lGODlhEAAQAIEAAP8AAAAAygCTCwAAACH5BAEAAAMALAAAAAAQABAAQAhWAAcIGDgggMGCBwEoFEhwoACEAQYoBCBx4cSKFC86hMhRI0GDEUFiHHmx5MKNG0V6fChS5cmPB11SHECzps2bJC3qnImzJ02UMCNe9OkzZcyEC4niDAgAOw=="))
        
        labelFont = tkFont.Font(family='Courier', size=8)
             
        self.canv = tk.Canvas(self.window, width=4*40 + 20, height=4*40 + 60,borderwidth=0, highlightthickness=0)
        self.btnSubmit = ttk.Button(self.window, text="Submit", command = self.guiSubmit, state='disable')
        self.btnAuto = ttk.Button(self.window, text="Auto", command = self.guiAuto)
        self.btnNewGame = ttk.Button(self.window, text="New Game", command = self.guiNewGame)
        self.label = tk.Label(self.window, width=32, font=labelFont, anchor="w", justify=tk.LEFT)

        self.canv.grid(row=0, column=0, padx=5, pady=5, rowspan=2)
        self.label.grid(row=0,column=1, padx=5, pady=5,sticky='n', columnspan=3)
        self.btnSubmit.grid(row=1, column=1, padx=5, pady=5, sticky='s')
        self.btnAuto.grid(row=1, column=2, padx=5, pady=5, sticky='s')
        self.btnNewGame.grid(row=1, column=3, padx=5, pady=5, sticky='s')
        
        for i in range(4):
            self.canv.create_rectangle(40*i+1,181,40*i+38,218,fill='',outline='azure3')
        
        self.guiGridCells = [[GuiTile(self.canv,x,y) for y in range(4)] for x in range(4)]
        self.guiHandCells = [GuiTile(self.canv,x-0.5,4.5,True) for x in range(4)]
        self.guiScores = [self.canv.create_text(4*40+10, 20+40*y, text='0') for y in range(4)] + \
                         [self.canv.create_text(x*40+20, 10+40*4, text='0',justify=tk.CENTER) for x in range(4)]                
        self.guiNewHand()

        self.canv.tag_bind("handTile", "<ButtonPress-1>", self.dragStart)
        self.canv.tag_bind("handTile", "<ButtonRelease-1>", self.dragStop)
        self.canv.tag_bind("handTile", "<B1-Motion>", self.dragMove)
        
        self._dragItem = None
        self._dragPos = None

        self.window.mainloop()
    
    def guiNewHand(self):
        # Update gui hand tile colours
        self.playLocations = np.array([(-1,-1)]*4)
        if len(self.hand) == 0:
            tileIDs = ['--']*4
        else:
            tileIDs = self.hand
        for i,c,e in zip(range(4), tileIDs, self.guiHandCells):
            e.setTile(c)
            e.moveTo(i*40, 180)

    def guiSubmit(self):
        next(self.currentGame)
        # update gui grid and discard cells from game data......
        for i,cVec in enumerate(self.guiGridCells):
            for j, c in enumerate(cVec):
                if self.grid[j,i] != '  ':
                    c.setTile(self.grid[j,i])
                    c.moveTo(i*40, j*40)

        # Construct score feedback strings
        self.guiUpdateScores()
        # Update button state and deal new hand
        self.btnSubmit["state"] = "disable"
        self.guiNewHand()

    def guiUpdateScores(self, scores=None):
        if scores is None:
            scores = self.scores
        scoreStr = ''
        for i,h in enumerate(self.guiScores):
            self.canv.itemconfig(h, text=scores[h-self.guiScores[0]]['score'])
            scoreStr = scoreStr + f"{scoreLabels[i]:<10}- "            
            scoreStr = scoreStr + f"{scores[i]['label']:<16}: {scores[i]['score']}\n"
            
        tot = sum([s['score'] for s in scores])
        scoreStr = scoreStr + '-'*32 + '\n' +' '*12+ f'{"Total:":<16}: {tot}'
        self.label.config(text=scoreStr)
        
    def guiAuto(self): 
        self.playLocations = self.autoPlay()
        self.guiSubmit()
    
    def guiNewGame(self):
        self.currentGame = self.playTurn()
        next(self.currentGame)
        for r in self.guiGridCells:
            for t in r:
                t.blank()
        for t in self.guiHandCells:
            t.blank()
        for h in self.guiScores:
            self.canv.itemconfig(h, text='0')
        self.label.config(text='')        
        self.guiNewHand()
        
    def dragStart(self, event):
        if not self.gameOver:
            item = self.canv.find_closest(event.x, event.y)[0]
            self._dragIndex = (item - self.guiHandCells[0].tile)//3
            self._dragTile = self.guiHandCells[self._dragIndex]
            self._dragTile.toTop()
            self._dragPos = (event.x, event.y)

    def dragStop(self, _):
        if not self.gameOver:
            x,y,_,_ = self.canv.coords(self._dragTile.tile)
            x = (int(x) + 20) // 40
            y = (int(y) + 20) // 40

            if x < 0 or y < 0 or x > 3 or y > 3 or self.grid[y,x] != '  ': # or len(self.playLocations) == 4:
                self._dragTile.moveTo(self._dragIndex*40, 180)
                self.playLocations[self._dragIndex,:] = np.array([-1,-1])
            else:
                iHandPlaced = np.argwhere((self.playLocations[:,0]==y) & (self.playLocations[:,1]==x))

                if np.size(iHandPlaced) > 0:
                    self.guiHandCells[iHandPlaced[0][0]].moveTo(iHandPlaced[0][0]*40, 180)
                    self.playLocations[iHandPlaced[0][0]]=[-1,-1]
                self._dragTile.moveTo(x*40,y*40)
                self.playLocations[self._dragIndex,:] = np.array([y,x])
                
            newGrid = self.grid.copy()
            for i,p in enumerate(self.playLocations):
                if np.all(p != -1):
                    newGrid[tuple(p)] = self.hand[i]
            scores = [self.getScore(i, newGrid) for i in range(8)]
            self.guiUpdateScores(scores)
            self.btnSubmit["state"] = "normal" if np.all(self.playLocations >= 0) else "disable"                    

    def dragMove(self, event):
        if not self.gameOver:
            dx,dy = event.x - self._dragPos[0], event.y - self._dragPos[1]
            self._dragTile.move(dx,dy)
            self._dragPos = (event.x, event.y)

class GuiTile:
    def __init__(self, canvas, x, y, isHandTile=False):
        tileFont = tkFont.Font(family='Courier', size=16, weight='bold')
        tileTag = ('handTile',) if isHandTile else None
        tileOutline = canvas['bg'] if isHandTile else 'azure'
        self.tile = canvas.create_rectangle(0,0,39,39,tags=tileTag,fill='azure4',outline=tileOutline)
        self.decor = canvas.create_polygon((0,0,0,37,37,37,37,0,0,0), tags=tileTag, width=4, outline='cyan',fill='')
        self.number = canvas.create_text(20,20,text='0',tags=tileTag,font=tileFont,fill='azure4')

        self.tileID = '--'
        self.canv = canvas
        self.isHandTile = isHandTile
        self.moveTo(x*40, y*40)
    def setTile(self, id):
        #if isinstance(id,str):
        if id=='--':
            self.blank()
        else:
            self.canv.itemconfig(self.tile, fill=cols[id[0]])
            self.canv.itemconfig(self.number, text=id[1])
            self.canv.itemconfig(self.number, fill='yellow' if self.isHandTile else 'white')
            self.tileID = id
    def blank(self):
        self.canv.itemconfig(self.tile, fill='azure4')
        self.canv.itemconfig(self.number, fill='azure4') 
        self.canv.itemconfig(self.decor, outline='azure4') 
        self.tileID = '--'
    def moveTo(self, x, y):
        self.canv.coords(self.number, x+20, y+20)
        self.moveDecorTo(x+20, y+20)
        #self.pos = (x, y)
    def move(self, dx, dy):
        self.canv.move(self.number, dx, dy)        
        x,y = self.canv.coords(self.number)
        self.moveDecorTo(x, y)
    def moveDecorTo(self,x,y):
        self.canv.coords(self.tile, x-20, y-20, x+19, y+19)
        dc = icons[self.tileID[0]] + np.array([x,y])
        self.canv.coords(self.decor, tuple(dc.flatten()))
        self.canv.itemconfig(self.decor, outline=iconCol[self.tileID[0]])
    def toTop(self):
        self.canv.tag_raise(self.tile)
        self.canv.tag_raise(self.decor)
        self.canv.tag_raise(self.number)
        
  
