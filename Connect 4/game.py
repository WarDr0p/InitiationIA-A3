import alphabeta

nbLignes = 6
nbCol = 12
class game:
    def __init__(self):
        self.nbLignes = 6
        self.nbColonnes = 12
        self.grille = [[0 for j in range(self.nbColonnes)] for i in range(self.nbLignes)]
        self.nbTours = 0
        self.ia = [0,0]
        print("Le joueur 1 (X) est un joueur (J) ou une IA (IA) :")
        entree : str
        entree = ""
        self.joueurs = [0,0]
        while 1:
            entree = input()
            if entree.upper() == "IA":
               self.joueurs[0] = 1
               self.ia[0] = alphabeta.IA(1,2,4)
               break
            elif entree.upper() == "J":
                self.joueurs[0] = 0
                break
            print('Merci de taper "IA" ou "J" :' )
        
        print("Le joueur 2 (O) est un joueur (J) ou une IA (IA) :")
        while 1:
            entree = input()
            if entree.upper() == "IA":
               self.joueurs[1] = 1
               self.ia[1] = alphabeta.IA(2,1,10)
               break
            elif entree.upper() == "J":
                self.joueurs[1] = 0
                break
            print('Merci de taper "IA" ou "J" :' )
    
    def __str__(self):
        sepl = "-".join("-" for i in range(self.nbColonnes))
        result = " ".join(" " if i+1 < 10 else str((i+1)//10) for i in range(self.nbColonnes))+"\n"
        result += " ".join( str((i+1)%10) for i in range(self.nbColonnes))+"\n"        
        for ligne in self.grille:
            result += "|".join("O" if car == 2 else "X" if car == 1 else " " if car == 0 else car for car in ligne)+"\n"
            result += sepl+"\n"
        return result
    
    def IsPlayable(self, column):
        if self.grille[0][column] == 0:
            return True
        return False
    
    def Start(self):
        symbol = ""
        print(TestTerminal(self.grille))
        while not TestTerminal(self.grille):
            print(self)
            if self.nbTours%2 :
                symbol = 2
            else : symbol = 1
            if self.joueurs[self.nbTours%2] == 0:
                self.getPlayerInput(symbol)
            else:
                self.ia[self.nbTours%2].Play(self.grille,5)
            self.nbTours +=1
        print(self)
        print("J",TestTerminal(self.grille)," gagne",sep="")
        if self.ia[0] != 0:
            print(self.ia[0].PrintStats())
        if self.ia[1] != 0:
            print(self.ia[1].PrintStats())
        
                
    def Play(self, column,symbol):
        played = False
        print(column)
        for i in range(self.nbLignes-1):
            if self.grille[i][column] == 0 and self.grille[i+1][column] != 0:
                self.grille[i][column] = symbol
                played = True
        if not played:
            self.grille[self.nbLignes-1][column] = symbol

    def getPlayerInput(self,symbol):
        while 1:
            print("Quelle colonne voulez jouer ?")
            entree : str
            entree = input()         
            if entree.isdigit() and float(entree)%1 == 0:
                if int(entree) > 0 and int(entree) <= self.nbColonnes:
                    if self.IsPlayable(int(entree)-1):
                        self.Play(int(entree)-1,symbol) 
                        break;
                    else:
                        print("Merci d'indiquer une colonne non pleine")
                else:
                    print("Merci d'entrer un entier inclus entre 0 et ",self.nbColonnes)
            else:
                print("Merci d'entrer un entier")

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


    
jeu = game()
jeu.Start()