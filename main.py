import Tkinter as tk
import time
import random

class App(tk.Frame):
    def __init__(self,myRoot):
        tk.Frame.__init__(self)
        self.root=myRoot
        myRoot.title('Caterpillar Game')
        myRoot.geometry('600x600')
        self.start=True
        self.gameOver=False
        myRoot.grid()
        self.createWidgetStart()
    
    def createWidgetStart(self):
        pic=tk.PhotoImage(file='caterpillar.gif')
        picLabel=tk.Label(self, image=pic)
        picLabel.pic=pic
        picLabel.grid(row=2, column=0)
        self.startButton=tk.Button(text='Start', command='')
        self.startButton.grid(row=3,column=2)


root= tk.Tk()
app=App(root)
app.mainloop()