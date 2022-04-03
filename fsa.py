# ----------------------------------------------------------------------------
# Student Name: Alan Benitez
# File Name: fsa.py
# Assignment number: Project 3
# In this file I read the input given in the program script, check if
# the string ends in the accept state and do the calls to draw the fsa
# ---------------------------------------------------------------------------

import sys
import tkinter as tk
from stateTransitions import fsaRep


class fsa:
    # Contructor
    def __init__(self, fsaFile, inputString):
        self.fsaFile = fsaFile
        self.inputString = inputString

    # Reads the files
    def readFile(self, fileName):
        fileString = ""
        with open(fileName) as f:
            fileString = f.read().replace(" ", "")
        return fileString

    # Checks if the string input is correct
    def checkGraph(self, node, remainder):
        if node < len(state_list) and node > -1:
            if len(remainder) == 1:
                return state_list[state_list[node].getNext(remainder[0])].accept
            return self.checkGraph(state_list[node].getNext(remainder[0]), remainder[1:])
        else:
            print("Error")
            exit(0)

    # Checks if FSA is correct and display the GUI
    def displayFSA(self, numberOfStates, acceptState, startState, stateTransitions, alphabet):
        global state_list
        state_list = []
        for i in range(numberOfStates):
            state_list.append(fsaRep(i, i == start, i in acceptState))
        for t in stateTransitions:
            if t[2] in alphabet:
                if int(t[0]) >= numberOfStates or int(t[1]) >= numberOfStates:
                    print("State does not exist")
                    exit(0)
                state_list[int(t[0])].setTransition(t[2], t[1])
            else:
                print("Character is not valid", t[2])
                exit(0)
        checkString = self.checkGraph(startState, self.readFile(self.inputString))
        if checkString == 1:
            print("Valid Input String")
        else:
            print("Illegal Input String")
        
        # Display the GUI
        root = tk.Tk()
        canvas = tk.Canvas(root, width=300, height=700, borderwidth=0, highlightthickness=0, bg = "white")
        for s in state_list:
            s.drawState(canvas)
        canvas.pack()
        root.mainloop()


if __name__ == "__main__":

    fsaFile = sys.argv[1]
    inputString = sys.argv[2]
    myFsa = fsa(fsaFile, inputString)
    numberOfStates, alphabet, stateTransition, startState, acceptState = myFsa.readFile(myFsa.fsaFile).split(';')[:-1]
    numberOfStates = int(numberOfStates)
    alphabet = alphabet.strip().split(',')
    stateTransition = [t[1:-1].split(':') for t in stateTransition.split(',')]
    acceptState = [int(i) for i in acceptState.split(',')]
    start = int(startState)
    myFsa.displayFSA(numberOfStates, acceptState, start, stateTransition, alphabet)
    