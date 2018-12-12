from random import *
'''
    Ce fichier python concerne la partie logique du jeu, il contient les fonctions de mouvements, d'ajout de tuile ...
'''

def init_partie(n):
    '''
    Initialisation de la  sur une nouvelle partie (de taille n, pour tetris : columns,lines)
    '''
    grille = []
    for i in range(n):
        grille.append([0] * n)
    return grille


def ajouterTuile(grille):
    '''
    Ajoute une case de valeur 2, sur une position aléatoire dans la taille correspondante
    a la grille, et dans une coordonnée ne contenant pas déjà une valeur différente de 0
    0 étant une case libre (sans tuile).
    '''
    x=randint(0,len(grille)-1)
    y=randint(0,len(grille)-1)
    while(grille[x][y]!=0):
        x=randint(0,len(grille)-1)
        y=randint(0,len(grille)-1)
    alea = randint(1,12)
    if alea<=4 or alea>=8:
        grille[x][y]= 2
    elif alea == 5 or alea==7:
        grille[x][y] = 4
    else:
        grille[x][y] = 8
    return grille

def etat(grille):
    '''
    A chaque étape, un état de la partie actuelle est contrôlée.
    * Si une case contient une valeur égale à 2048, l'utilisateur gagne.
    * Si il reste une solution dans une grille complète, l'utilisateur ne perd pas
    * Si il reste une case avec une valeur égale à 0 (équivalante à case vide), l'utilisateur n'as pas perdu.
    * Si il reste une solution dans la grille, pas terminé pour les 2 derniers for.
    * Si aucun test ne retourne une réponse, alors il retourne perdu, signifiant qu'aucune des conditions de victoires/coups à jouer n'est validés.
    '''
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==32768:
                return 'Gagné'
    for i in range(len(grille)-1):
        for j in range(len(grille[0])-1):
            if grille[i][j]==grille[i+1][j] or grille[i][j+1]==grille[i][j]:
                return 'Pas terminé'
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==0:
                return 'Pas terminé'
    for i in range(len(grille)-1):
        if grille[len(grille)-1][i]==grille[len(grille)-1][i+1]:
            return 'Pas terminé'
    for j in range(len(grille)-1):
        if grille[j][len(grille)-1]==grille[j+1][len(grille)-1]:
            return 'Pas terminé'
    return 'Perdu'

def inversion(grille):
    '''
    B = A⁻¹,
    telle que :
    AB = BA = In
    Fonction utilisable uniquement sur grille carrée.
    '''
    temp=[]
    for i in range(len(grille)):
        temp.append([])
        for j in range(len(grille[0])):
            temp[i].append(grille[i][len(grille[0])-j-1])
    return temp

def transposer(grille):
    '''
    La transposée AT d'une grille A s'obtient par symétrie axiale par rapport à la diagonale principale de la grille.
    La transposée de la transposée (AT)T est la grille A d'origine.
    '''
    temp=[]
    for i in range(len(grille[0])):
        temp.append([])
        for j in range(len(grille)):
            temp[i].append(grille[j][i])
    return temp

def grilleSecondaire(grille):
    temp=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    statut_action=False
    for i in range(len(grille)):
        compt=0
        for j in range(len(grille)):
            if grille[i][j]!=0:
                temp[i][compt]=grille[i][j]
                if j!=compt:
                    statut_action=True
                compt+=1
    return (temp,statut_action)


def fusion(grille):
    '''
    Le code de fusion gère la fusion de cellule, si la position [i][j] == [i][j+1], alors on multiplie la valeur de [i][j]*2
    '''
    statut_action=False
    for i in range(len(grille)):
         for j in range(len(grille)-1):
             if grille[i][j]==grille[i][j+1] and grille[i][j]!=0:
                 grille[i][j]*=2
                 grille[i][j+1]=0
                 statut_action=True
    return (grille,statut_action)

def up(grille):
        grille=transposer(grille)
        grille,statut_action=grilleSecondaire(grille)
        temp=fusion(grille)
        grille=temp[0]
        statut_action=statut_action or temp[1]
        grille=grilleSecondaire(grille)[0]
        grille=transposer(grille)
        return (grille,statut_action)

def down(grille):
        grille=inversion(transposer(grille))
        grille,statut_action=grilleSecondaire(grille)
        temp=fusion(grille)
        grille=temp[0]
        statut_action=statut_action or temp[1]
        grille=grilleSecondaire(grille)[0]
        grille=transposer(inversion(grille))
        return (grille,statut_action)

def left(grille):
        grille,statut_action=grilleSecondaire(grille)
        temp=fusion(grille)
        grille=temp[0]
        statut_action=statut_action or temp[1]
        grille=grilleSecondaire(grille)[0]
        return (grille,statut_action)

def right(grille):
        grille=inversion(grille)
        grille,statut_action=grilleSecondaire(grille)
        temp=fusion(grille)
        grille=temp[0]
        statut_action=statut_action or temp[1]
        grille=grilleSecondaire(grille)[0]
        grille=inversion(grille)
        return (grille,statut_action)
