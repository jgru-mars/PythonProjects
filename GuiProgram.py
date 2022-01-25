# Josiah Groux
# This is a dino gui program

import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound

# This creates the tkinter window with background color and size
wn = tk.Tk()
wn.geometry('1000x460')
wn.configure(bg="grey")

# when the Trex button is clicked it will change the image and text in the label box
def onClickRex():
    txtDinoDesc.config(text="T-Rex, King of Dino")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/trex.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# when the Stegosaurus button is clicked it will change the image and text in the label box
def onClickSteg():
    txtDinoDesc.config(text="Stegosaurus, The Dude")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/steg.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# when the Triceratops button is clicked it will change the image and text in the label box
def onClickTri():
    txtDinoDesc.config(text="Triceratops, Spiky")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/tri.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# when the Amargasaurus button is clicked it will change the image and text in the label box
def onClickAma():
    txtDinoDesc.config(text="Amargasaurus, as you do")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/weirdDino.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# when the Kosmoceratops button is clicked it will change the image and text in the label box
def onClickKos():
    txtDinoDesc.config(text="Kosmoceratops, with a K")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/cosmo.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# when the Rhinorex button is clicked it will change the image and text in the label box
def onClickRhino():
    txtDinoDesc.config(text="Rhinorex, It is")
    imgCharacter = ImageTk.PhotoImage((Image.open("img/rhino.jfif")))
    lblImage['image'] = imgCharacter
    lblImage.image = imgCharacter

# in the process of making it play music, it does but will not open the tkinter window until the song is done. Working on a fix
# def playSounds():
#   playsound("music/jurassicPark.wav")

# this function chooses a random number from a list and the number is a assigned to one of the buttons, acting as if they were selected
def onRandom():
    numberList=(0,1,2,3,4,5)
    randomNumber = random.choice(numberList)
    if randomNumber == 0:
        onClickRex()
    elif randomNumber == 1:
        onClickSteg()
    elif randomNumber == 2:
        onClickTri()
    elif randomNumber == 3:
        onClickAma()
    elif randomNumber == 4:
        onClickKos()
    elif randomNumber == 5:
        onClickRhino()
    else:
        print("You should not get me.")

# the following creates the buttons in the program
trexButton = tk.Button(wn,width = 20, text="Tyrannosaurus", command=onClickRex)
trexButton.grid(row=0, column=1)
stegButton = tk.Button(wn,width = 20, text="Stegosaurus",command=onClickSteg)
stegButton.grid(row=0, column=2)
triButton = tk.Button(wn,width = 20, text="Triceratops",command=onClickTri)
triButton.grid(row=2, column=2)
amaButton = tk.Button(wn,width = 20, text="Amargasaurus",command=onClickAma)
amaButton.grid(row=1, column=1)
kosButton = tk.Button(wn,width = 20, text="Kosmoceratops",command=onClickKos)
kosButton.grid(row=1, column=2)
rhinoButton = tk.Button(wn,width = 20, text="Rhinorex",command=onClickRhino)
rhinoButton.grid(row=2, column=1)
randomButton = tk.Button(wn,width = 20,height=20, text="Random",command=onRandom)
randomButton.grid(row=3, column=1)
yeaButton = tk.Button(wn,width = 20,height=20, text="yea, this here to look nice") # ,command=playSounds()
yeaButton.grid(row=3, column=2)

# creates the label text box on the left side of the tkinter window
txtDinoDesc = tk.Label(wn, width = 30, height = 20, text="Choose a Dinosaur", borderwidth=1,relief="solid")
txtDinoDesc.grid(row = 3, column = 0)

# creates the first image used in the tkinter window.
lblImage = tk.Label(wn)
lblImage.grid(row=3, column=10)
imgCharacter = ImageTk.PhotoImage((Image.open("img/weirdDino.jfif")))
lblImage['image'] = imgCharacter
lblImage.image = imgCharacter

wn.mainloop()
