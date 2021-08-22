from tkinter import *
import random

class DrewsButton:
    def __init__(self, master):                     #master is the root or main window for the gui
        frame = Frame(master)
        one = Label(root, text="Welcome to my dice simulator", bg="black", fg="white")  #title on the top
        one.pack(fill=Y)
        frame.pack()

        self.printButton =Button(frame, text="Roll dice ", bg="blue", fg="white", command=self.dicefunction) #colors, and text of the button
        self.printButton.pack(side=LEFT)                                        #puts the button towards the left side

        self.quitButton = Button(frame, text="Quit",bg="black", fg="red", command=frame.quit)
        self.quitButton.pack(side=LEFT)                                         #since something is already on the left of it, this goes on the right

    def dicefunction(event):
        rd1 = random.randint(1, 6)
        rd2 = random.randint(1, 6)
        roll = rd1 + rd2
        print(f'Your first dice gave a result of: {rd1}')
        print(f'Your second dice gave a result of: {rd2}')
        print(f'Move {roll} spaces ')
root = Tk()                                                     #this is a constructor and root creates a blank window
b = DrewsButton(root)
root.mainloop()                                                 #loops the window and allows it to keep the window open
