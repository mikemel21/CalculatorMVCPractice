# used for GUI; included in python
import tkinter as tk
# better looking buttons and interface
from tkinter import ttk

class View(tk.Tk):
    # stores how many buttons I can have in each row
    MAXBUTTONROWS = 4
    # padding for the window; creates a gap between the frame and window
    PADDING = 10

    # stores the button labels in the order/place they will be in; allows me to dynamically create the buttons
    buttonLabels = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__() # calls initialized method of base class (gives access to Tkinter import)
        self.controller = controller

        self.title("MVC Assignment Calculator")

        # stores input from entry
        self.valueVar = tk.StringVar()
        
        self.mainFrame()
        self.createEntry()
        self.createButtons()

    # create the main GUI frame/window
    def mainFrame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PADDING, pady=self.PADDING)
    
    # adds text box that displays the button you pressed; cannot type in it
    def createEntry(self):
        entry = ttk.Entry(self.main_frame, justify='right', textvariable=self.valueVar)
        entry.pack(fill='x')

    # instantiate buttons
    def createButtons(self):
        # create a frame within the main frame to store all the buttons
        outerFrame = ttk.Frame(self.main_frame)
        outerFrame.pack()

        # create frames within outer frame for each row
        innerFrame = ttk.Frame(outerFrame)
        innerFrame.pack()

        buttonsInRows=0

        # dynamically create buttons
        for i in self.buttonLabels:
            # creates a new row if the max button amount is hit
            if buttonsInRows == self.MAXBUTTONROWS:
                innerFrame = ttk.Frame(outerFrame)
                innerFrame.pack()
                buttonsInRows = 0
            
            bt = ttk.Button(innerFrame, text=i)
            bt.pack(side = 'left')
            buttonsInRows += 1

    def main(self):
        #main loop of GUI
        self.mainloop()