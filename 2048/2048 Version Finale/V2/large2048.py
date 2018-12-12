from tkinter import *
from fonction import *
from random import *
from tkinter.messagebox import *
import sys

'''
Pour LEN_GRILLE, si on modifie la valeur, ainsi que la valeur introduite dans init_partie(n) avec n > 4, modifié également les boucles for dans logic.py pour adaptation
'''
LEN_GRILLE = 8
PADDING_GRILLE = 2 # Espace entre les cellules

'''
* Définition des couleurs backgrounds par type de cellules et par valeurs de cellules via l'utilisation de dictionnaires
* Définition de la police d'écriture, sa taille et son type.
* Définition des touches up,down,left,right attribuée à z,s,q,d
'''
FONT = ("Trebuchet", 20, "bold")
KEY_UP = "'z'"
KEY_DOWN = "'s'"
KEY_LEFT = "'q'"
KEY_RIGHT = "'d'"
BG_GRILLE = "#2A251F"
BG_CELLULE_VIDE = "#3F372F"
DICO_BG_CELLULE = {   2:"#FAF1E8", 4:"#DACAAB", 8:"#D3F37A", 16:"#CEF368", \
                            32:"#A8D03C", 64:"#8FB22F", 128:"#3662DB", 256:"#2C51B9", \
                            512:"#8F52F7", 1024:"#7B43DC", 2048:"#DC4343"}
DICO_FG_CELLULE = { 2:"#7B6F62", 4:"#7B6F62", 8:"#7B6F62", 16:"#7B6F62", \
                    32:"#F7F3EE", 64:"#F7F3EE", 128:"#F7F3EE", 256:"#F7F3EE", \
                    512:"#F7F3EE", 1024:"#F7F3EE", 2048:"#F7F3EE" }



class Grille2048(Frame):
    def __init__(self):
        '''
        Lancement et initialisation, définition des actions de commandes.
        '''
        Frame.__init__(self)
        self.grid() # Création du gestionnaire de positionnement, découpage en grille.
        self.master.title('Projet S2 large 2048 : Michel | El Hadad | Merveille | Doutrelon | Nique')
        self.master.bind("<Key>", self.partie)
        self.commands = {   KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right}
        self.cellule_grille = []    #Liste initialiser pour stocker les cellules de la grille
        self.init_interface()
        self.init_grille()
        self.maj_cellule()
        self.mainloop()

    def init_interface(self):
        '''
        Création de la grille, attribution de la couleur de fond + par cellule vide et attribution font+options
        '''
        background = Frame(self, bg=BG_GRILLE)
        background.grid()
        for i in range(LEN_GRILLE):
            rangee_grille = []
            for j in range(LEN_GRILLE):
                case = Frame(background, bg=BG_CELLULE_VIDE)
                case.grid(row=i, column=j, padx=PADDING_GRILLE, pady=PADDING_GRILLE)
                t = Label(master=case, text="", bg=BG_CELLULE_VIDE, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                rangee_grille.append(t)
            self.cellule_grille.append(rangee_grille)

    def init_grille(self):
        '''
        init_grille() crée et initialise la grille du 2048 avec 2 cellules de valeur 2 ou 4 au départ.
        '''
        self.grille = init_partie(LEN_GRILLE)
        self.grille=ajouterTuile(self.grille)
        self.grille=ajouterTuile(self.grille)

    def maj_cellule(self):
        '''
        Mise à jour des cellules (couleurs/valeurs)
        '''
        for i in range(LEN_GRILLE):
            for j in range(LEN_GRILLE):
                valeur_cellule = self.grille[i][j]
                if valeur_cellule == 0:
                    self.cellule_grille[i][j].configure(text="", bg=BG_CELLULE_VIDE)
                else:
                    self.cellule_grille[i][j].configure(text=str(valeur_cellule), bg=DICO_BG_CELLULE[valeur_cellule], fg=DICO_FG_CELLULE[valeur_cellule])

    def partie(self, event):
        '''
        Une touche a été pressée : tests, actions dédiées et statut de la partie en cours
        '''
        commande = repr(event.char)
        if commande in self.commands:
            self.grille,statut_action = self.commands[repr(event.char)](self.grille)
            if statut_action:
                self.grille = ajouterTuile(self.grille)
                self.maj_cellule()
                statut_action = False
                if etat(self.grille)=='Gagné':
                    question = askretrycancel("Rejouer ?","Vous avez gagné ! Bravo ! Voulez vous rejouer ?")
                    if question:
                        self.destroy()
                        partie = Grille2048()
                    else:
                        sys.exit(0)
                if etat(self.grille)=='Perdu':
                    question = askretrycancel("Rejouer ?","Vous avez perdu ! Dommage ! Voulez vous rejouer ?")
                    if question:
                        self.destroy()
                        partie = Grille2048()
                    else:
                        sys.exit(0)

root=Tk()
root.resizable(False,False)

partie = Grille2048()
