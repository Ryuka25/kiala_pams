
#======================================================#
#-------------Définition des fonctions-----------------#
#======================================================#

def fileToDico(filepath):

    #Affectation des variables!

    scoreDico = {} #Dictionnaire pour récevoir les scores et les noms!

    file=open(filepath, "r")

    for lines in file: #boucles permettant de parcourir les lignes du fichier texte.

        #Formatages des lignes
        lines = lines.split(" ")
        scores = lines[0]
        names = str(lines[1].replace("\n", " "))

        #Remplissage du dictionnaire:
        scoreDico[names] = scores
        
        #Retour finale!
    return scoreDico

def dicoToFile(scoreDico,filepath):
    scoreList = []
    with open(filepath, "w") as file:
        for keys in scoreDico:
            scoreList.append(f"{scoreDico[keys]} {keys}\n")
        file.writelines(scoreList)

def dicoToOrderList(scoreDico):
    scores = []#initialisation du liste SCORES
    scoresInit = [] #Dépot pour la liste initiale!
    orderNames = [] #Initialisation du liste pour les noms ordonées!
    orderList = [] #Initialisation du liste triée

    names = list(scoreDico.keys())
    for name in names: #Sort chaque nom contenu dans la liste des "keys" du Dico
        scores = scores + [int(scoreDico.get(name))]#Sort les score assiée à chaque Joueur dans l'ordre des joueurs!

    scoresInit += scores
    scores.sort()

    for ordScoreIterator in range(len(scores)):
        scoreIterator = 0
        #Compare les éléments du scores ordonée avec les scores non ordonée
        #pour trouver le nom ordonée! à chaque correspondance, le terminale rétourne le nom qui corréspond à la bonne ordre @Ryuka25
        while scores[ordScoreIterator] != scoresInit[scoreIterator]:    
                scoreIterator += 1
        orderNames = orderNames + [names[scoreIterator]]

    i = len(names)-1
    while (i+1)>0:
        orderList.append("{} {}".format(scores[i], orderNames[i]))
        i -= 1
    return orderList
    
#======================================================#
#--------------------FIN FONCTIONS---------------------#
#======================================================#
