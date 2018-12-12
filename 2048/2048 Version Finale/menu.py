#!/usr/bin/python3

from tkinter import *
from tkinter.messagebox import *
import sys
import os


fenetre = Tk()
fenetre.title("PROJET S2 | DOUTRELON | EL HADAD | MERVEILLE | MICHEL | NIQUE")
fenetre.config(bg = "#57407C")
fenetre.resizable(False,False)
photo = PhotoImage(file="2048.gif")
canvas = Canvas(fenetre,width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

def callback():
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):
        showinfo('Quitter', 'Dommage...')
        fenetre.quit()
    else:
        showinfo('Quitter', 'Allez battre le meilleur score lol!!')

def V1():
	systeme = os.name
	if systeme == "nt":
		com = "cmd /K python ./V1/2048.py %s"
	elif systeme == "posix":
		com = "xterm -e python3 ./V1/2048.py %s"
	os.system(com)

def V2():
	systeme = os.name
	if systeme == "nt":
		com = "cmd /K python ./V2/large2048.py %s"
	elif systeme == "posix":
		com = "xterm -e python3 ./V2/large2048.py %s"
	os.system(com)

def V3():
	systeme = os.name
	if systeme == "nt":
		com = "cmd /K python ./V3/32k.py %s"
	elif systeme == "posix":
		com = "xterm -e python3 ./V3/32k.py %s"
	os.system(com)

def V4():
	systeme = os.name
	if systeme == "nt":
		com = "cmd /K python ./V4/tetris2048.py %s"
	elif systeme == "posix":
		com = "xterm -e python3 ./V4/tetris2048.py %s"
	os.system(com)

def classement():
	pass

Button(fenetre, text =' Version 2048 original ',command=V1,width=20).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text =' Version large 2048 8x8 ',command=V2,width=20).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text =' Version 32K',command=V3,width=20).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text =' Version Tetris 2048',command=V4,width=20).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text =' Classement ',width=20).pack(side=TOP, padx=5, pady=5)
Button(text=' Fermer ', command=callback).pack(side=TOP, padx=5, pady=5)

fenetre.mainloop()
