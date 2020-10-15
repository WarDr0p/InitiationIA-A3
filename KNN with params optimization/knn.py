import math
import random
import matplotlib.pyplot as plt

#Retourne le mode d'une liste cad l'occurence la plus représentée
def mode(liste):
    dico = {liste.count(i):i for i in liste}
    return dico[max(dico)]
    
#Retourne la distance euclidienne entre 2 points de dimension N
def DistanceEuclidienne(p1, p2):
    return math.sqrt(sum([math.pow(p1[i]-p2[i],2) for i in range(len(p1))]))

#Récupère les données du csv et les range dans un tableau
def GetData(name):
    file = open(name,"r")
    data = []
    for ligne in file:
        if ligne != "\n":    
            temp = ligne.split(";")
            val = temp[4].replace("\n","")
            temp = [float(temp[i]) for i in range(4)]
            data.append([temp,val])
    return data

def GetTest():
    file = open("finalTest.csv","r")
    data = []
    for ligne in file:
        if ligne != "\n":    
            temp = ligne.split(";")
            temp = [float(temp[i].replace(";",'')) for i in range(4)]
            data.append(temp)
    return data

def ReturnClassif():
    file = open("outputExample_FORESTIER_HAHUSSEAU.txt","w")
    atester = GetTest()
    training = GetData("final.csv")    
    for ech in atester:
        val = knn(training,ech,5,False)
        print(val)
        file.write(val+"\n")
    file.close()
    print("export terminé")

#Permet de générer un dataset de test et un dataset d'apprentissage
def Separate(data):
    train = []
    test = []
    for i in data:   
        if random.random() < 0.75:
            train.append(i)
        else:
            test.append(i)        
    return train,test

def knn(data, test, k, printResult):
    tab = []
    #Calcul de la distance Euclidienne
    for echantillon in data:
        tab.append([DistanceEuclidienne(echantillon[0],test),echantillon])
    tab.sort()

    result = []
    #On récupère les k premires
    for i in range (k):
        result.append(tab[i][1][1])
    return mode(result)


def knnParamFinder(data, test, printResult, maxk,stat):
    tab = []
    #Calcul de la distance Euclidienne
    for echantillon in data:
        tab.append([DistanceEuclidienne(echantillon[0],test[0]),echantillon])
    tab.sort()

    result = []
    #On récupère les k premirs
    for i in range (maxk):
        result.append(tab[i][1][1])
        if mode(result)==test[1]:
            stat[i] +=1


def findOptimalParam(name,maxK, nbIt):
    data = GetData(name);
    stat = [0 for i in range(maxK)]
    for i in range (nbIt):
        train,test = Separate(data)
        if i%10 == 0:
            print(i)
        for ech in test:
            knnParamFinder(train,ech,False,maxK,stat)
    plt.plot(stat)
    plt.show()
    print("Maximum de bonne réponses",max(stat))
    print("Atteint pour k =",stat.index(max(stat)))
    return stat

ReturnClassif()