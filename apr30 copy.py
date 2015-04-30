# Mazy Game App

import Tkinter as tk
import random

sizeOfMazeCell = 30
wallColor='light coral'
mazeColor='white'
difficulty = 'Easy'  # 'Easy', 'Medium', or 'Hard'

class Cell:
    def __init__(self):
        pass
        
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.M = []
        for i in range(height):
            self.M.append([])
            for j in range(width):
                self.M[i].append(Cell())    


class MazyApp(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.width = 20
        self.height = 20
        self.MZ = Maze(self.width, self.height)
        self.title('Mazy Game')
        self.grid()
        self.createWidgets()

    def setMazeLabel(self, theImage, clr, row, col):
        self.mazeLabels[row][col].destroy()
        self.mazeLabels[row][col] = tk.Label(self, image=theImage, bg=clr, width=sizeOfMazeCell, height=sizeOfMazeCell)
        self.mazeLabels[row][col].theImage = theImage
        self.mazeLabels[row][col].grid(row=row,column=col,sticky=tk.N+tk.E+tk.W+tk.S)
    
    def setMazyLabel(self):
        row = self.mazyPosition[0]
        col = self.mazyPosition[1]
        self.setMazeLabel(self.mazyImage, mazeColor, row, col)


    def placeFood(self):
        self.homeImage = tk.PhotoImage(file='igloo.gif')
        self.homePosition = (random.randint(0,19), random.randint(0,19))  # Position of food
        self.setMazeLabel(self.homeImage, mazeColor, self.homePosition[0], self.homePosition[1])

    def bindArrowKeys(self):
        self.bind('<Left>', self.leftKey)  # When left arrow key is pressed, invoke self.leftKey method
        self.bind('<Right>', self.rightKey)  # When right arrow key is pressed, invoke self.rightKey method
        self.bind('<Up>', self.upKey)  # When up arrow key is pressed, invoke self.upKey method
        self.bind('<Down>', self.downKey)  # When down arrow key is pressed, invoke self.downKey method

    def unbindArrowKeys(self):
        self.unbind('<Left>')
        self.unbind('<Right>')
        self.unbind('<Up>')
        self.unbind('<Down>')
        
    
    #def move(self, dirRow, dirCol):
    #    self.directionRow = dirRow #store direction for next time event
    #    self.directionColumn = dirCol
    #    newHeadRow = self.headRow + dirRow
    #    newHeadCol = self.headCol + dirCol
    #    if newHeadRow < 0 or newHeadRow >= boardRows or newHeadCol < 0 or newHeadCol >= boardCols:
    #        # runs off the board
    #        self.gameOver = True
    #    elif [newHeadRow,newHeadCol] in self.coordinates:
    #        #runs into itself
    #        self.gameOver = True
    #    elif [newHeadRow,newHeadCol] == self.foodCoor:
    #        # eating food!
    #        self.coordinates.append([newHeadRow,newHeadCol])
    #        self.headRow = newHeadRow
    #        self.headCol = newHeadCol
    #        placeFood()
    #    else:
    #        # normal move forward (not eating food)
    #        self.coordinates.append([newHeadRow,newHeadCol])
    #        self.headRow = newHeadRow
    #        self.headCol = newHeadCol
    #        self.coordinates = self.coordinates [1:]
            
    def leftKey(self, event):
        row = self.mazyPosition[0]
        col = self.mazyPosition[1]
        self.mazyPosition = (row, col-1)
        self.handleGameOver()
        self.setMazeLabel(self.emptyImage,mazeColor,row,col)
        self.setMazyLabel()
        

    def rightKey(self, event):
        row = self.mazyPosition[0]
        col = self.mazyPosition[1]
        self.mazyPosition = (row, col+1)
        self.handleGameOver()
        self.setMazeLabel(self.emptyImage,mazeColor,row,col)
        self.setMazyLabel()
                
    def upKey(self, event):
        row = self.mazyPosition[0]
        col = self.mazyPosition[1]
        self.mazyPosition = (row-1, col)
        self.handleGameOver()
        self.setMazeLabel(self.emptyImage,mazeColor,row,col)
        self.setMazyLabel()

    def downKey(self, event):
        row = self.mazyPosition[0]
        col = self.mazyPosition[1]
        self.mazyPosition = (row+1, col)
        self.handleGameOver()
        self.setMazeLabel(self.emptyImage,mazeColor,row,col)
        self.setMazyLabel()
        


    def eatFood(self):
        return (self.mazyPosition[0]==self.homePosition[0]) and (self.mazyPosition[1]==self.homePosition[1])
        
    def hitWall(self):
        return (self.mazyPosition[0] not in range(0,19)) or (self.mazyPosition[1] not in range(0,19))
        
    def runIntoSelf(self):
        return (self.mazyPosition in self.coordinates)


    def handleGameOver(self):
        
        if self.hitWall():
            self.gameOver = True
            self.statusText = 'Oops, Game Over.'
            self.status.set(self.statusText)
            self.unbindArrowKeys()
            
        elif self.runIntoSelf(self):
            #runs into itself
            self.statusText = 'Oops, Game Over.'
            self.status.set(self.statusText)
            self.unbindArrowKeys()
            
        elif self.eatFood():
            # eating food!
            self.score += 1
            self.statusText = 'Weeeeeee! Current Score = ' + str(self.score)
            self.status.set(self.statusText)
            self.placeFood()
            
 
        
        #else:
        #    # normal move forward (not eating food)
        #    self.coordinates.append([newHeadRow,newHeadCol])
        #    self.headRow = newHeadRow
        #    self.headCol = newHeadCol
        #    self.coordinates = self.coordinates [1:]
        #
        

                                      
    def createWidgets(self):

        # Maze labels        
        self.mazeLabels = []
        self.emptyImage = tk.PhotoImage()  # Empty image so Label width and height are in pixels
        for i in range(self.height):
            self.mazeLabels.append([])
            for j in range(self.width):
                self.mazeLabels[i].append(tk.Label(self,image=self.emptyImage,bg=wallColor,width=sizeOfMazeCell,height=sizeOfMazeCell))
                clr = mazeColor
                self.setMazeLabel(self.emptyImage,clr,i,j)

        # Home image and MaZy image
        
        self.placeFood()
        self.mazyImage = tk.PhotoImage(file='penguin3.gif')
        self.mazyPosition = (1,1)  # MaZy's current position
        self.coordinates = [(1,1)]
        self.setMazyLabel()

        # Status label   
        self.status = tk.StringVar()
        self.statusLabel = tk.Label(self,bg=wallColor,fg=mazeColor,font='Verdana 18',textvariable=self.status)
        self.score = 0
        self.statusText = 'Current Score = ' + str(self.score)
        self.status.set(self.statusText)
        self.statusLabel.grid(row=self.height,columnspan=self.width,sticky=tk.N+tk.E+tk.W+tk.S)

        # Movement with arrow keys
        self.bindArrowKeys()


class StarterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.m_app = None
        self.title('Mazy Game Startup Window')
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        easyButton = tk.Button(self, fg='red', bg='yellow', text='Start!', command=self.onEasyButtonClick)
        easyButton.grid(row=0,sticky=tk.N+tk.E+tk.W+tk.S)

    
    def onEasyButtonClick(self):
        
        if self.m_app!=None: self.m_app.destroy()  # Destroy existing maze app
        self.m_app = MazyApp()
        self.m_app.mainloop()

    
app = StarterApp()
app.mainloop()
