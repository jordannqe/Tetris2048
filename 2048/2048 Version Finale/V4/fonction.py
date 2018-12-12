from random import *

'''
    Ce fichier python concerne la partie logique du jeu, il contient les fonctions de mouvements, d'ajout de tuile ...
'''

score = 0
LEN_GRILLE_WIDTH = 5
LEN_GRILLE_HEIGHT = 8

'''
def definirGrille():
    largeur = int(input("Largeur de la grille : "))
    hauteur = int(input("Hauteur de la grille : "))
    while largeur>hauteur:
        print("Erreur, veuillez définir une largeur inférieur à la hauteur de la grille :")
        largeur = int(input("Largeur de la grille : "))
        hauteur = int(input("Hauteur de la grille : "))
    while (hauteur-largeur) > 3:
        print("Erreur, différence hauteur-largeur trop élevée :")
        largeur = int(input("Largeur de la grille : "))
        hauteur = int(input("Hauteur de la grille : "))
    return (largeur,hauteur)

LEN_GRILLE_WIDTH,LEN_GRILLE_HEIGHT = definirGrille()
'''

def init_partie(n,p):
    '''
    Initialisation de la matrice sur une nouvelle partie (de taille n, pour tetris : columns,lines)
    '''
    grille = []

    for i in range(n):
        for j in range(p):
            grille.append([0] * p)
    return grille

def ajouterTuile(grille):
    '''
    Ajoute une case de valeur 2, sur une position aléatoire dans la taille correspondante
    a la matrice, et dans une coordonnée ne contenant pas déjà une valeur différente de 0
    0 étant une case libre (sans tuile).
    '''
    x = 0
    y = randint(0,LEN_GRILLE_WIDTH-1)
    while(grille[x][y]!=0):
        y = randint(0,LEN_GRILLE_WIDTH-1)
    alea = randint(1,12)
    if alea<=4 or alea>=8:
        grille[x][y]= 2
    elif alea == 5 or alea==7:
        grille[x][y] = 4
    else:
        grille[x][y] = 8
    return grille

def addTuileDepart(grille):
    '''
    Ajoute une case de valeur 2, sur une position aléatoire dans la taille correspondante
    a la matrice, et dans une coordonnée ne contenant pas déjà une valeur différente de 0
    0 étant une case libre (sans tuile).
    '''
    x = LEN_GRILLE_HEIGHT-1
    y = randint(0,LEN_GRILLE_WIDTH-1)
    while(grille[x][y]!=0):
        y = randint(0,LEN_GRILLE_WIDTH-1)
    alea = randint(1,12)
    if alea<=4 or alea>=8:
        grille[x][y]= 2
    else:
        grille[x][y] = 4
    return grille

def calcul_score(score_temp,puissance):
    '''
    Calcul du score à chaque fusion de cellules
    '''
    score_temp = score_temp + puissance * 10
    return score_temp

def etat(grille):
    '''
    Parcours de la matrice, si une coordonnée x,y == 2048 alors il retourne vrai sinon rien.
    '''
    for x in range(len(grille)):
        for y in range(len(grille[0])):
            if grille[x][y]==2048:
                return True
    return False

def fusion_col(grille,x,y):
    '''
    fusion_col permet de fusionner après chaque tour de tuile, une colonne (et de faire descendre le reste)
    '''
    for i in range(1,x-1):
        grille[x+1-i][y] = grille[x-i][y]
    grille[1][y] = 0
    grille[x][y] *= 2

def fusion_line(grille,x,y):
    '''
    fusion_line permet de fusionner après chaque tour de tuile, une ligne (et de faire aller le reste vers la droite) (Convention décidée)
    '''
    for i in range(0,y):
        grille[x][y-i] = grille[x][y-i-1]
    grille[x][0] = 0
    grille[x][y] *= 2

def down(grille):
    tempVar1 = 0
    tempVar2 = 0
    for i in range(LEN_GRILLE_WIDTH):
        if grille[0][i] != 0:
            tempVar1 = i
            for j in range(LEN_GRILLE_HEIGHT):
                if grille[j][i] == 0:
                    tempVar2 = j
    grille[tempVar2][tempVar1] = grille[0][tempVar1]
    grille[0][tempVar1] = 0
    statut_action = True
    return (grille,statut_action)

def left(grille):
    temp = 0
    for i in range(1,LEN_GRILLE_WIDTH): #parcourir la ligne 0 et les colonnes de la ligne 0
        if grille[0][i] != 0:
            temp = i
    if temp >= 2:
        grille[0][temp-1] = grille[0][temp]
        grille[0][temp] = 0
    elif temp==1:
        grille[0][temp-1] = grille[0][temp]
        grille[0][temp] = 0
    statut_action = True
    return (grille,statut_action)

def right(grille):
    temp = 0
    for i in range(LEN_GRILLE_WIDTH-1): #parcourir la ligne 0 et les colonnes de la ligne 0
        if grille[0][i] != 0:
            temp = i
    if temp == len(grille[0])-1:
        grille[0][0] = grille[0][temp]
        grille[0][temp] = 0
    else:
        grille[0][temp+1] = grille[0][temp]
        grille[0][temp] = 0
    statut_action = True
    return (grille,statut_action)
