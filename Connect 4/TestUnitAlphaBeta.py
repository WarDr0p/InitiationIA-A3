# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:39:04 2020

@author: Alexandre
"""
import alphabeta
ia1 = alphabeta.IA("X","O",7)
ia2 = alphabeta.IA("O","X",7)
def testUtility(ia):
    x = "X"
    a = "O"

    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [x,0,0,0,0,0,0,0,0,0,0,0],
              [0,x,0,0,0,0,0,0,0,0,0,0],
              [0,0,x,0,0,0,0,0,0,0,0,0],
              [0,0,0,x,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,x,0,0,0],
              [0,0,0,0,0,0,0,0,0,x,0,0],
              [0,0,0,0,0,0,0,0,0,0,x,0],
              [0,0,0,0,0,0,0,0,0,0,0,x],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,x],
              [0,0,0,0,0,0,0,0,0,0,x,0],
              [0,0,0,0,0,0,0,0,0,x,0,0],
              [0,0,0,0,0,0,0,0,x,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,x,0,0,0,0,0,0,0,0],
              [0,0,x,0,0,0,0,0,0,0,0,0],
              [0,x,0,0,0,0,0,0,0,0,0,0],
              [x,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,x,0,0,0,0,0,0,0,0],
              [0,0,0,0,x,0,0,0,0,0,0,0],
              [0,0,0,0,0,x,0,0,0,0,0,0],
              [0,0,0,0,0,0,x,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,x,0,0,0,0,0,0,0,0],
              [0,0,x,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [x,x,x,x,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [a,0,0,0,0,0,0,0,0,0,0,0],
              [x,0,0,0,0,0,0,0,0,0,0,0],
              [x,0,0,0,0,0,0,0,0,0,0,0],
              [x,0,0,0,0,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    
    grille = [[x,a,x,a,x,a,x,a,x,a,x,a],
              [x,a,x,a,x,a,x,a,x,a,x,a],
              [x,a,x,a,x,a,x,a,x,a,x,a],
              [a,x,a,x,a,x,a,x,a,x,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0]]    
    print(ia.Utility(grille))
    
    grille = [[0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0],
              [a,x,x,0,a,0,0,0,0,0,0,0]]
    print(ia.Utility(grille))
    print("done test terminal")

#testUtility(ia1)
#testUtility(ia2)

