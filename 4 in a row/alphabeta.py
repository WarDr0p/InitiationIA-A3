import alphabeta
import time
import copy
import math
from utils import TestTerminal
from matplotlib import pyplot as plt

class IA:    
    def __init__(self,symbolIA,symbolP,depth):
        self.symbolIA = symbolIA
        self.symbolP = symbolP
        self.memory = []
        self.stop = round(time.perf_counter(),2)
        self.previousGrid = []
        self.utility = []
        self.memory = []
    
    def VerifAlignement(self,grid,i,j,a,b):
        symbol = ""
        count =[0,0,0,0,0,0]
        changes = [0,0,0,0,0,0]
        cpt2 = 0
        cpt = 0
        while i >= 0 and j >=0 and i < len(grid) and j < len(grid[0]):
            if grid[i][j]==0:
                cpt2+=1
            elif grid[i][j]==symbol:
                cpt+=1
                cpt2+=1
                if cpt == 2:               
                    if symbol == 0:
                        cpt = 1
                    elif symbol == self.symbolIA:
                        count[0] += 1
                        changes[0] +=1
                    else:
                        count[1] += 1
                        changes[1] +=1
                if cpt == 3:
                    if symbol == 0:
                        cpt = 1
                    elif symbol == self.symbolIA:
                        count[2] += 1
                        changes[2] +=1
                    else:
                        count[3] += 1
                        changes[3] +=1
                if cpt ==4:
                    if symbol == 0:
                        cpt = 1
                    elif symbol == self.symbolIA:
                        count[4] += 1
                        changes[4] +=1
                    else:
                        count[5] += 1
                        changes[5] +=1
            else:
                if cpt2<4:
                     count = [count[i] - changes[i] for i in range(6)]
                cpt = 1
                cpt2 = 1
                changes = [0,0,0,0,0,0]
                symbol = grid[i][j]
            i+=a
            j+=b
        if cpt2<4:
            count = [count[i] - changes[i] for i in range(6)]
                     
        if count[0]>0 or count[1]>0:
            return count
        return False
    
    def CheckGagnant(self,grid):
        #lignes
        result = [0,0,0,0,0,0]
        nbLignes = len(grid)
        nbCol = len(grid[0])
        #print("lignes")
        for i in range(nbLignes):
            boole = self.VerifAlignement(grid,i,0,0,1)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        #colonne
        for j in range(nbCol):
            boole = self.VerifAlignement(grid,0,j,1,0)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        #Diag desc 1
        for i in range(0,nbLignes-2+1):
            boole = self.VerifAlignement(grid,i,0,1,1)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        #Diag desc 2
        for j in range(1,nbCol-2+1):
            boole = self.VerifAlignement(grid,0,j,1,1)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        #Diag mont 1
        for i in range(2-1,nbLignes):
            boole = self.VerifAlignement(grid,i,0,-1,1)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        #Diag mont 2
        for j in range(0, nbCol-3):
            boole = self.VerifAlignement(grid,nbLignes-1,j,-1,1)
            if boole:
                result[0]+=boole[0]
                result[1]+=boole[1]
                result[2]+=boole[2]
                result[3]+=boole[3]
                result[4]+=boole[4]
                result[5]+=boole[5]
        if(result[0]>0 or result[1]>0):
            return result
        return False
    
    def Action(self,grid):
        result = []
        j = 6
        for j in [6,5,7,4,8,3,9,2,10,1,11,0]:
            for i in range(len(grid)-1,-1,-1):
                if grid[i][j]==0:
                    if j > 0 and grid[i][j-1] != 0:
                        result.append([i,j])
                        break
                    elif j < len(grid[0])-1 and grid[i][j+1] !=0:
                        result.append([i,j])
                        break
                    elif j > 1 and grid[i][j-2] != 0:
                        result.append([i,j])
                        break
                    elif j < len(grid[0])-2 and grid[i][j+2] != 0:
                        result.append([i,j])
                        break
                    elif i < len(grid)-1 and grid[i+1][j] != 0:
                        result.append([i,j])
                        break
        if len(result)==0:
            result.append([len(grid)-1,int(len(grid[0])/2)])
        return result
    
    def Utility(self,grid,depth=0):
        
        val = self.CheckGagnant(grid)
        if val == False:
            return 0
        else:
            return(2*val[0]+6*val[2]+100*min(val[4],1) - 2*val[1]-6*val[3]-100*min(val[5],1))
    
    def Result(self,grid,a,symbol):
        grid[a[0]][a[1]] = symbol
        return grid

    def MinValueAlphaBeta(self,state, alpha,beta,depth,case):
        if TestTerminal(state) or depth == 0:
            return self.Utility(state,depth)
        v = math.inf
        for a in self.Action(state):
            v = min(v,self.MaxValueAlphaBeta(self.Result(copy.deepcopy(state),a,self.symbolP),alpha,beta,depth-1,case))
            beta = min(beta,v)
            if beta<=alpha:
                break
        return v
    
    def MaxValueAlphaBeta(self,state, alpha, beta,depth,case):
        if TestTerminal(state) or depth == 0:
            return self.Utility(state,depth)
        v = -math.inf
        for a in self.Action(state):
            v = max(v,self.MinValueAlphaBeta(self.Result(copy.deepcopy(state),a,self.symbolIA),alpha,beta,depth-1,case))
            alpha = max(alpha,v)
            if beta<=alpha:
                break            
        return v
    
    def AlphaBetaDecision(self,state,depth):
        temps = time.perf_counter()
        actions = self.Action(state)
        values = [self.MinValueAlphaBeta(self.Result(copy.deepcopy(state),a,self.symbolIA),-math.inf,math.inf,depth,a) for a in actions]
        print(actions)
        print(values)
        self.utility.append(max(values))
        result = actions[values.index(max(values))]
        print("Temps = ",round(time.perf_counter()-temps,2))
        print("l'IA a joué colonne",result[1])
        return result
    
    def Play(self, state,depth):
        action = self.AlphaBetaDecision(state,depth)
        state[action[0]][action[1]] = self.symbolIA
        self.previousGrid = state
        
                        
        
    def PrintStats(self):
        plt.plot(self.utility)
        plt.title("Evolution of utility over time")
        plt.xlabel("Turn number")
        plt.ylabel("Utility value (greatest is better)")
        plt.show()
        
    
    
        