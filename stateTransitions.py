#----------------------------------------------------------------------------
# Student Name: Alan Benitez
# File Name: stateTransitions.py
# Assignment number: Project 3
# In this file I do the GUI 
# ---------------------------------------------------------------------------

import tkinter as tk

class fsaRep:

    # Constructor
    def __init__(self, id, start, accept):
        self.map = {}
        self.id = id
        self.start = start
        self.accept = accept
        self.y = self.updateYaxis 

    def updateYaxis(self, y):
        return y*100+100

    # Sets the transition to a state
    def setTransition(self, input, output):
        self.map[input] = int(output)

    # Getter for next state
    def getNext(self, c):
        return self.map[c]

    # Draws the lines for the fsa
    def drawLines(self, canvas, x, dia):
        for i, j in self.map.items():
            # Arrow pointing to the same state
            if abs(self.id-j) == 0:
                canvas.create_line(x+dia, self.y(self.id)+dia/4, x+(dia*2), self.y(self.id)-2*dia, x+(dia*2), self.y(j)+dia*2, x+dia, self.y(j), smooth =1, arrow=tk.LAST)
                canvas.create_text(x+50, self.y(self.id), text=i)
            # Arrow pointing dows
            if abs(self.id-j) == 1:
                canvas.create_line(x, self.y(self.id)-dia, x, self.y(self.id)+100-dia, arrow=tk.LAST)
                canvas.create_text(x+dia-5, self.y(self.id) + (2*dia), text=i)

            # Arrow pointing up
            if abs(self.id-j) > 1:
                global up
                up = 0
                temp = up
                canvas.create_line(x, self.y(self.id), x+up-(dia*3), self.y(self.id), x+up-(dia*3), self.y(j), x-dia, self.y(j), arrow=tk.LAST)
                canvas.create_text(x+up-(dia*4), ((self.y(j)-self.y(self.id))/2)+self.y(self.id), text=i)
                up = temp + 25
  
        

    # Draws the states of the fsa
    def drawState(self, canvas):
        x = 110
        dia = 20 #diameter
        if self.start:
            canvas.create_line(x, self.y(self.id)-100, x,
                               self.y(self.id)-dia, arrow=tk.LAST)
            canvas.create_text(x+dia, self.y(self.id)-(2*dia), text="start")
        self.drawLines(canvas, x, dia)
        canvas.create_oval(x-dia, self.y(self.id)-dia, x+dia, self.y(self.id)+dia, fill="white")
        canvas.create_text(x, self.y(self.id), text=str(self.id))
