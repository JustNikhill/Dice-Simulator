# INSTALL FOLLOWING PIP

import tkinter                                 
from PIL import Image, ImageTk
import random

#  represents the main window of an application

root = tkinter.Tk()
root.geometry('400x400')
root.title('DataFlair Roll the Dice')

# Adding label into the frame

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting

HeadingLabel = tkinter.Label(root, text="Nikhil's Dice simulator",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()

#  for images

dice = ['die1.png', 'die2.png', 'die3.png',
    'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between 0 to 6 and generating image

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget

ImageLabel.pack( expand=True)

#  for images

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))




root.mainloop()                  # keeps window open




