# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:35:00 2020

@author: Alexandre

Réponses aux questions :
    
1) Hormis k, quels autres paramètres ou modiﬁcations pourrait-on apporter aﬁn de modiﬁer le comportement de l’algorithme?
On peut jouer sur la norme utilisée, dans ce cas on utilise la norme euclidienne mais il existe beaucoup d'autre type de normes.
On pourrait aussi trier par ordre décroissant afin de dé-classifier une image (savoir ce qu'elle n'est pas)

2) Quelle modiﬁcation apporter aﬁn d’utiliser l’algorithme en régression plutôt qu’en classiﬁcation?
Plutôt que de prendre le mode des knn on pourrait prendre leur moyenne
"""


"""
KNN
"""

import math
import random

#Retourne le mode d'une liste cad l'occurence la plus représentée
def mode(liste):
    dico = {liste.count(i):i for i in liste}
    return dico[max(dico)]
    
#Retourne la distance euclidienne entre 2 points de dimension N
def DistanceEuclidienne(p1, p2):
    return math.sqrt(sum([math.pow(p1[i]-p2[i],2) for i in range(len(p1))]))

#Récupère les données du csv et les range dans un tableau
def GetData():
    file = open("iris.data","r")
    data = []
    for ligne in file:
        if ligne != "\n":    
            temp = ligne.split(",")
            val = temp[4].replace("\n","")
            temp = [float(temp[i]) for i in range(4)]
            data.append([temp,val])
    return data

#Permet de générer un dataset de test et un dataset d'apprentissage
def Separate(data):
    train = []
    test = []
    for i in range(len(data)):
        if i % 2 :
            train.append(data[i])
        else:
            test.append(data[i])         
    return train,test


def knn(data, test, k, printResult):
    tab = []
    #Calcul de la distance Euclidienne
    for echantillon in data:
        tab.append([DistanceEuclidienne(echantillon[0],test[0]),echantillon])
    tab.sort()

    result = []
    #On récupère les k premirs
    for i in range (k):
        result.append(tab[i][1][1])
    
    #On affcihe les résultats
    if printResult:
        print("Predicted :",mode(result),"Percentage :",round(float(result.count((mode(result))))*100/float(k),1), "\nReal answer :",test[1])
    return mode(result)


def getConfusionmatrix(k):
    #On crée un dictionnaire pour faciliter le classement dans le tableau
    dico = {"Iris-versicolor":0,"Iris-virginica":1,"Iris-setosa":2}
    matrix = [[0 for i in range(3)] for j in range(3)]
    data,test = Separate(GetData());
    for echantillon in test:
        i = dico[echantillon[1]]
        j = dico[knn(data,echantillon,k,False)]
        matrix[i][j]+=1
        
    print("\n\n\n\nMatrice de confusion :\n")
    print("     Classe estimée par le classificateur   ")
    print("           |versicolor | virginica | setosa")
    print("versicolor |    ",end ='')
    print(*matrix[0],sep = "     |     ")
    print("virginica  |     ",end ='')
    print(*matrix[1],sep = "     |     ")
    print("  setosa   |     ",end ='')
    print(*matrix[2],sep = "     |     ")

"""
DBSCAN
Les pourcentages de chaques classes sont donnés à titre indicatif à aucun moment ils ne rentrent en jeu dans la répartition des données
"""
def dbscan(D, eps, MinPts):
    print("\n\n\n\n DBSCAN")
    c = 0
    #on rajoute une case pour le cluster et la visite
    #On marque les points comme non visités
    for ligne in D:
        ligne.append(0)
        ligne.append(0)
    for ligne in D:
        #On vérifie que le point n'a pas été visité
        if ligne[2]==0:
            ligne[2] = 1
            PtsVoisins = epsilonVoisinage(D,ligne,eps)
            if len(PtsVoisins) < MinPts:
                ligne[2] = 2
            else:
                c +=1
                etendreCluster(D,ligne,PtsVoisins, c, eps, MinPts)
    printResult(D)
            
def etendreCluster(D,P,PtsVoisins,c,eps,MinPts):
    P[3] = c
    for pv in PtsVoisins:
        if pv[2] == 0:
            pv[2] = 1
            PtsVoisinsp = epsilonVoisinage(D,pv,eps)
            if len(PtsVoisinsp) >= MinPts:
                PtsVoisins = Union(PtsVoisins, PtsVoisinsp)
            if pv[3]==0:
                pv[3] = c 
    
def Union(e1,e2):
    result = []
    for liste2 in e2:
        egal = True
        for liste1 in e1:
            egal = True
            for i in range(len(liste1[0])):
                if liste1[0][i] != liste2[0][i]:
                    #On break car on a trouvé une différence avec un point donc il est différent de ce point
                    egal = False
                    break
            if egal == True:
                #On break car on a trouvé un point égal à P dans la liste 1 donc pas la peine de l'ajouter à nouveau
                break;
        if egal != True:
            result.append(liste1)
    return e1+result;

def epsilonVoisinage(D,P,eps):
    result = []
    for point in D:
        if DistanceEuclidienne(point[0], P[0])<eps and point[2]==0:
            result.append(point)
    return result

def printResult(data):
    val = []
    for elem in data:
        if val.count(elem[3]) == 0:
            val.append(elem[3])
    
    print("Classes générées par dbscan")
    print("Numéro de classe | taille | mode | %")
    val.sort()
    for cluster in val:
        cpt = 0
        iris = []
        for elem in data:
            if elem[3] == cluster:
                cpt+=1
                iris.append(elem[1])
        classe = cluster
        if cluster < 10:
            classe = " "+str(cluster)
        cpt2 = cpt
        if cpt < 10:
            cpt2 = " "+str(cpt)
        if cluster == 0:
            classe = "Bruit"
        print(classe,"|",cpt2,"|",mode(iris),"|",round(iris.count(mode(iris))*100/cpt),"%")
        
        if cluster == 0:
            print("\n")

print("KNN\n")
data,test = Separate(GetData());
choix = random.randrange(0,len(test))
print("échantillon n° :",choix,"extrait du batch de test")
knn(data, test[choix], 30, True)    
    
getConfusionmatrix(10)
  
dbscan(GetData(),1,5)
