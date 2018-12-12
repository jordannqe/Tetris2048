from tkinter import *
from fonction import *
from random import *
from tkinter.messagebox import *
import sys
from time import *

'''
* Définition des touches up,down,left,right attribuée à z,s,q,d
* Définition des couleurs backgrounds par type de cellules et par valeurs de cellules via l'utilisation de dictionnaires
* Définition de la police d'écriture, sa taille et son type.
'''
PADDING_GRILLE = 2 # Espace entre les cellules


KEY_UP = "'z'"
KEY_DOWN = "'s'"
KEY_LEFT = "'q'"
KEY_RIGHT = "'d'"


BG_GRILLE = "#2A251F"
BG_CELLULE_VIDE = "#3F372F"
DICO_BG_CELLULE = {   2:"#FAF1E8", 4:"#DACAAB", 8:"#D3F37A", 16:"#CEF368",
                            32:"#A8D03C", 64:"#8FB22F", 128:"#3662DB", 256:"#2C51B9", \
                            512:"#8F52F7", 1024:"#7B43DC", 2048:"#DC4343" }
DICO_FG_CELLULE = { 2:"#7B6F62", 4:"#7B6F62", 8:"#7B6F62", 16:"#7B6F62", \
                    32:"#F7F3EE", 64:"#F7F3EE", 128:"#F7F3EE", 256:"#F7F3EE", \
                    512:"#F7F3EE", 1024:"#F7F3EE", 2048:"#F7F3EE" }
FONT = ("Trebuchet", 20, "bold")
FONT2 = ("Trebuchet", 14, "bold")
FG_SCORE = "#F7F3EE"


class Grille2048(Frame):
    def __init__(self):
        '''
        Lancement et initialisation, définition des actions de commandes.
        '''
        Frame.__init__(self)
        self.text = Label(text="Score :", bg=BG_CELLULE_VIDE, fg=FG_SCORE, justify=CENTER, font=FONT2, width=32, height=1)
        self.text.grid() # Création du gestionnaire de positionnement, découpage en grille.
        self.textScore = Label(text="0", bg=BG_CELLULE_VIDE, fg=FG_SCORE, justify=CENTER, font=FONT2, width=32, height=1)
        self.textScore.grid()
        self.grid()
        self.master.title('Projet S2 2048 Tetris : Michel | El Hadad | Merveille | Doutrelon | Nique')
        self.master.bind("<Key>", self.partie)

        self.commands = {   KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right}
        self.score = 0              #Init score
        self.cellule_grille = []    #Liste initialiser pour stocker les cellules de la grille
        self.init_interface()
        self.init_grille()
        self.maj_cellule()

        liste_score = []
        bestScore = 0
        with open("./V4/score.txt","r") as score_read:
            for scoreListe in score_read:
                liste_score = scoreListe.split(",")

            if len(liste_score)>0:
                del liste_score[len(liste_score)-1]
                liste_score = [int(i) for i in liste_score]
                bestScore = max(liste_score, default=0)
            else:
                bestScore=0
        #print(liste_score) #print la liste des scores du fichier texte

        self.bestScore = Label(text="Meilleur score : "+ str(bestScore), bg=BG_CELLULE_VIDE, fg=FG_SCORE, justify=CENTER, font=FONT2, width=32, height=1)
        self.bestScore.grid()

        self.mainloop()

    def init_interface(self):
        '''
        Création de la grille, attribution de la couleur de fond + par cellule vide et attribution font+options
        '''
        background = Frame(self, bg=BG_GRILLE)
        background.grid()
        for i in range(LEN_GRILLE_HEIGHT):
            rangee_grille = [] # initialisation d'une rangée
            for j in range(LEN_GRILLE_WIDTH):
                case = Frame(background, bg=BG_CELLULE_VIDE)
                case.grid(row=i, column=j, padx=PADDING_GRILLE, pady=PADDING_GRILLE)
                t = Label(master=case, text="", bg=BG_CELLULE_VIDE, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                rangee_grille.append(t)

            self.cellule_grille.append(rangee_grille)

    def update_score(self,score):
        self.textScore.config(text=str(self.score))



    def init_grille(self):
        '''
        init_grille() crée et initialise la grille du 2048 avec 2 cellules de valeur 2 ou 4 au départ.
        '''
        self.grille = init_partie(LEN_GRILLE_WIDTH,LEN_GRILLE_HEIGHT)
        self.grille = ajouterTuile(self.grille)
        self.grille = addTuileDepart(self.grille)


    def maj_cellule(self):
        '''
        Mise à jour des cellules (couleurs/valeurs)
        '''
        for i in range(LEN_GRILLE_HEIGHT):
            for j in range(LEN_GRILLE_WIDTH):
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
        if commande == KEY_DOWN:
            for i in range(LEN_GRILLE_WIDTH):
                if self.grille[0][i] != 0 and self.grille[1][i] != 0 and self.grille[0][i] != self.grille[1][i]:

                    question = askretrycancel("Rejouer ?","Vous avez perdu ! Dommage ! Voulez vous rejouer ?")
                    if question:
                        with open("./V4/score.txt","a") as score_file:
                            score_file.write(str(self.score)+",")
                        self.destroy()
                        self.text.destroy()
                        self.textScore.destroy()
                        self.bestScore.destroy()
                        partie = Grille2048()
                    else:
                        with open("./V4/score.txt","a") as score_file:
                            score_file.write(str(self.score)+",")
                        sys.exit(0)
                elif self.grille[0][i] != 0 and self.grille[1][i] != 0 and self.grille[0][i] == self.grille[1][i]:
                    self.grille[0][i] = 0
                    self.grille[1][i] *= 2
        if commande in self.commands:
            self.grille,statut_action = self.commands[repr(event.char)](self.grille)
            if statut_action:
                statut_fusion = True
                l = LEN_GRILLE_WIDTH
                h = LEN_GRILLE_HEIGHT
                while statut_fusion:
                    '''
                    Permet de lancer les programmes de fusions de cellules tant qu'il y a deux cellules minimum à fusionner. (Fusion tour à tour)
                    '''
                    statut_fusion = False
                    for a in range(1,h-1):
                        for b in range(1,l+1):
                            if self.grille[h-a][l-b] == self.grille[h-a-1][l-b] and self.grille[h-a][l-b] != 0:
                                fusion_col(self.grille,h-a,l-b)
                                statut_fusion = True
                                self.score = calcul_score(self.score,self.grille[h-a][l-b])
                            elif self.grille[h-a][l-b] == self.grille[h-a][l-b-1] and self.grille[h-a][l-b] != 0:
                                fusion_line(self.grille,h-a,l-b)
                                statut_fusion = True
                                self.score = calcul_score(self.score,self.grille[h-a][l-b])
                    statut_down = True
                    while statut_down:
                        '''
                        Permet de descendre les tuiles si, après des fusions, une cellule se retrouve sans cellule inférieure (exemple cellule = 4, cellule inférieure = 0, 0 étant le vide)
                        '''
                        statut_down = False
                        for a in range(1,LEN_GRILLE_HEIGHT-1):
                            for b in range(0,LEN_GRILLE_WIDTH):
                                if self.grille[a][b] != 0 and self.grille[a+1][b] == 0:
                                    self.grille[a+1][b] = self.grille[a][b]
                                    self.grille[a][b] = 0
                                    statut_down = True

                if commande == KEY_DOWN:
                    self.update_score(score)
                    self.grille = ajouterTuile(self.grille)
                self.maj_cellule()
                statut_action=False
                if etat(self.grille):
                    question = askretrycancel("Rejouer ?","Vous avez gagné ! Bravo ! Voulez vous rejouer ?")
                    if question:
                        with open("./V4/score.txt","a") as score_file:
                            score_file.write(str(self.score)+",")
                        self.destroy()
                        self.text.destroy()
                        self.textScore.destroy()
                        self.bestScore.destroy()
                        partie = Grille2048()
                    else:
                        with open("./V4/score.txt","a") as score_file:
                            score_file.write(str(self.score)+",")
                        sys.exit(0)

root = Tk()
root.resizable(False,False)

partie = Grille2048()
