import Tkinter as tk
import time
import random

class App(tk.Frame):
    def __init__(self,myRoot):
        tk.Frame.__init__(self)
        self.root=myRoot
        myRoot.title('Caterpillar Game')
        myRoot.geometry('600x500')
        self.start=True
        self.gameOver=False
        self.grid()
        self.createWidgetStart()
    
    def createWidgetStart(self):
        pic=tk.PhotoImage(file='caterpillar.gif')

        picLabel=tk.Label(self,image=pic)
        picLabel.pic=pic
        picLabel.grid(row=1, column=1)
        self.startButton=tk.Button(self,text='Start')
        self.startButton.grid(row=10,column=1)


root= tk.Tk()
app=App(root)
root.mainloop()

#
#import random
#import Tkinter  as tk

boardRows = 10
boardCols = 10
self.coordinates = []
self.foodCoor = []



def changeDir(self, event):
    canvas = event.widget.canvas
    # now process keys that only work if the game is not over
    if self.gameOver == False :
        if (event.keysym == "Up"):
            move(canvas, -1, 0)
        elif (event.keysym == "Down"):
            move(canvas, +1, 0)
        elif (event.keysym == "Left"):
            move(canvas, 0,-1)
        elif (event.keysym == "Right"):
            move(canvas, 0,+1)
    redrawAll(canvas)



def move(self, dirRow, dirCol):
    self.directionRow = dirRow #store direction for next time event
    self.directionColumn = dirCol
    newHeadRow = self.headRow + dirRow
    newHeadCol = self.headCol + dirCol
    if newHeadRow < 0 or newHeadRow >= boardRows or newHeadCol < 0 or newHeadCol >= boardCols:
        # runs off the board
        self.gameOver = True
    elif [newHeadRow,newHeadCol] in self.coordinates:
        #runs into itself
        self.gameOver = True
    elif [newHeadRow,newHeadCol] == self.foodCoor:
        # eating food!
        self.coordinates.append([newHeadRow,newHeadCol])
        self.headRow = newHeadRow
        self.headCol = newHeadCol
        placeFood()
    else:
        # normal move forward (not eating food)
        self.coordinates.append([newHeadRow,newHeadCol])
        self.headRow = newHeadRow
        self.headCol = newHeadCol
        self.coordinates = self.coordinates [1:]
