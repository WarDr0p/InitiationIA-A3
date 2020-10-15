# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:37:28 2020

@author: Alexandre
"""
nbLignes = 6
nbCol = 12

def VerifAlignementTestTerminal(grid,i,j,a,b):
    symbol = grid[i][j]
    cpt = 0
    while i >= 0 and j >= 0 and j < nbCol and i < nbLignes:
        if grid[i][j]==symbol:
            cpt+=1
            if cpt == 4:         
                if symbol == 0:
                    cpt = 1
                else : return symbol
        else:
            cpt = 1
            symbol = grid[i][j]
        i += a
        j += b
    return False

def CheckGagnantTestTerminal(grid):
    #print("lignes")
    for i in range(nbLignes):
        boole = VerifAlignementTestTerminal(grid,i,0,0,1)
        if boole:
            return boole
    #print("colonnes")
    #colonne
    for j in range(nbCol):
        boole = VerifAlignementTestTerminal(grid,0,j,1,0)
        if boole:
            return boole
    #print("diag1")
    #Diag desc 1
    for i in range(0,nbLignes-3):
        boole = VerifAlignementTestTerminal(grid,i,0,1,1)
        if boole:
            return boole
    #print("diag2")
    #Diag desc 2
    for j in range(1,nbCol-3):
        boole = VerifAlignementTestTerminal(grid,0,j,1,1)
        if boole:
            return boole
    #Diag mont 1
    #print("diag3")
    for i in range(2,nbLignes):
        boole = VerifAlignementTestTerminal(grid,i,0,-1,1)
        if boole:
            return boole
    #Diag mont 2
    #print("diag4")
    for j in range(0, nbCol-3):
        boole = VerifAlignementTestTerminal(grid,nbLignes-1,j,-1,1)
        if boole:
            return boole
    return False

def TestTerminal(grille):
    val = CheckGagnantTestTerminal(grille)
    if val:
        return CheckGagnantTestTerminal(grille)
    else:
        cpt = 0
        for ligne in grille:
            for case in ligne:
                if case:
                    cpt+=1
                    if cpt > 41:
                        return True
    return False

