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