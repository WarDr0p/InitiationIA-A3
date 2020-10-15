"""
Created on Sat Mar  7 14:11:00 2020
@author: Alexandre
"""
import random

def AfficherGrille(gridInit):
    for i in gridInit:
        print(i)

def ColonneOk(gridInit,j,val):
    for case in gridInit:
        if case[j] == val:
            return False
    return True

def LigneOk(gridInit,i,val):
    for case in gridInit[i]:
        if case == val:
            return False
    return True

def CarreOk(gridInit,i,j,val):
    for ligne in range(i-i%3,i-i%3+3):
        for colonne in range(j-j%3,j-j%3 +3):
            if gridInit[ligne][colonne] == val:
                return False
    return True

def InitialiserGrille(mode):
    gridInit = [[0 for i in range(9)] for j in range (9)]
    cases = list(range(9))
    choices = [case + 1 for case in cases ]

    for i in range(17):
        i = 0
        j = 0
        val = 0
        pasTrouve = True
        while pasTrouve:
            occupe = True
            while occupe:
                i = random.choice(cases)
                j = random.choice(cases)
                if gridInit[i][j] == 0:
                    occupe = False
            val = random.choice(choices)
            if ColonneOk(gridInit, j,val) and LigneOk(gridInit, i,val) and CarreOk(gridInit,i,j,val):
                pasTrouve = False
        gridInit[i][j] = val
    return gridInit
        
def Resolveur(gridInit):
    from ortools.sat.python import cp_model
    contraintes = cp_model.CpModel()
    #On déclare les valeurs que peut prendre chaque case
    grid = [[contraintes.NewIntVar(1,9," ") for i in range (9)] for j in range(9)] 
    
    #maintenant on déclare nos contraintes au solveur on commence par les lignes
    for ligne in grid:
        contraintes.AddAllDifferent([case for case in ligne])   
        
    #passage aux colonnes
    for j in range(9):
        contraintes.AddAllDifferent([ ligne[j] for ligne in grid])  
        
    #Les carrés   
    for i in range(3):
        for j in range(3):
            contraintes.AddAllDifferent(grid[3*i+offsetI][3*j+offsetJ] for offsetI in range(3) for offsetJ in range(3))
    
    #On précise les valeurs d'initialisation
    for i in range(9):
        for j in range(9):
            if gridInit[i][j]!=0:
                contraintes.Add(grid[i][j] == gridInit[i][j])
     #On résoud           
    solution = cp_model.CpSolver()
    statut = solution.Solve(contraintes)
    result = []
    if statut == cp_model.FEASIBLE:
        for i in range(9):
            result.append([int(solution.Value(grid[i][j])) for j in range(9)])
        return result
    else :
        return -1
    
def RemoveCases:    
    if mode == 0 or mode == "débutant":
        nbCases = 50
    elif mode == 1 or mode == "facile":
        nbCases == 40
    elif mode == 2 or mode == "moyen":
        nbCases == 33
    elif mode == 3 or mode == "difficile":
        nbCases == 26
    
result = -1
while result == -1:
    init = InitialiserGrille(1)
    result = Resolveur(init)         
print("===== Départ =====")
AfficherGrille(init)
print("===== Résultat =====")
AfficherGrille(result)       