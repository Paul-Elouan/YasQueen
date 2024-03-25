import time
import copy

N = 8

class TabGrille:
    def __init__(self):
        self.nbSoluce = 0
        self.solutions = list()

def initialiser_grille():
    return [[0] * N for _ in range(N)]

def ajouter_solution(grille, tab):
    tab.solutions.append(copy.deepcopy(grille))
    tab.nbSoluce += 1

def est_valide(grille, ligne, colonne):
    # Vérifier la ligne
    for i in range(colonne):
        if grille[ligne][i] == 1:
            return False

    # Vérifier la diagonale supérieure gauche
    for i, j in zip(range(ligne, -1, -1), range(colonne, -1, -1)):
        if grille[i][j] == 1:
            return False

    # Vérifier la diagonale inférieure gauche
    for i, j in zip(range(ligne, N, 1), range(colonne, -1, -1)):
        if grille[i][j] == 1:
            return False

    return True

def forward_checking(grille, ligne, colonne):
    for i in range(ligne + 1, N):
        if grille[i][colonne] == 1:
            return False

        diag_sup_gauche = colonne - (i - ligne)
        diag_inf_gauche = colonne + (i - ligne)

        if diag_sup_gauche >= 0 and grille[i][diag_sup_gauche] == 1:
            return False
        if diag_inf_gauche < N and grille[i][diag_inf_gauche] == 1:
            return False

    return True

def placer_reine(grille, colonne, tab):
    if colonne >= N:
        ajouter_solution(grille, tab)
        return True
    else:
        for i in range(N):
            if est_valide(grille, i, colonne) and forward_checking(grille, i, colonne):
                grille[i][colonne] = 1
                if placer_reine(grille, colonne + 1, tab):
                    grille[i][colonne] = 0  # Annuler la modification pour tester d'autres positions
                else:
                    grille[i][colonne] = 0  # Annuler la modification si la solution n'est pas possible
        return False

def afficher_grille(grid):
    for k in range(N):
        print("+---------", end="")
    print("+")
    for i in range(N):
        for k in range(3):
            for j in range(N):
                if grid[i][j] == 1:
                    if k == 0:
                        print("|   _O_   ", end="")
                    elif k == 1:
                        print("|   \\ /   ", end="")
                    elif k == 2:
                        print("|   /_\\   ", end="")
                    else:
                        print("|         ", end="")
                else:
                    print("|         ", end="")
            print("|")
        for k in range(N):
            print("+---------", end="")
        print("+")

def ecrire_fichier(tab):
    with open('solutions.txt', 'w') as f:
        for n in range(tab.nbSoluce):
            f.write("Solution " + str(n + 1) + ":\n")
            for k in range(N):
                f.write("+---------")
            f.write("+\n")
            for i in range(N):
                for k in range(3):
                    for j in range(N):
                        if tab.solutions[n][i][j] == 1:
                            if k == 0:
                                f.write("|   _O_   ")
                            elif k == 1:
                                f.write("|   \\ /   ")
                            elif k == 2:
                                f.write("|   /_\\   ")
                            else:
                                f.write("|         ")
                        else:
                            f.write("|         ")
                    f.write("|\n")
                for k in range(N):
                    f.write("+---------")
                f.write("+\n")
            f.write("\n")

def main():
    grille = initialiser_grille()
    tab = TabGrille()

    print("Calcul des solutions...")

    debut = time.time()

    placer_reine(grille, 0, tab)

    fin = time.time()
    temps_cpu = fin - debut

    print("{} solutions trouvees\nTemps CPU : {:.3f}".format(tab.nbSoluce, temps_cpu))

    choix = str()
    while choix != "4":
        print("\n1. Afficher toutes les solutions\n2. Afficher une solution\n3. Ecrire les solutions dans un fichier\n4. Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            for i in range(tab.nbSoluce):
                print("Solution ", i + 1)
                afficher_grille(tab.solutions[i])

        elif choix == "2":
            num = int(input("Entrez le numéro de la solution à afficher : "))
            if num > tab.nbSoluce or num < 1:
                print("Numéro de solution invalide !")
            else:
                print("Solution n°", num)
                afficher_grille(tab.solutions[num - 1])

        elif choix == "3":
            print("Ecriture des solutions dans le fichier \"solutions.txt\"...")
            ecrire_fichier(tab)

        elif choix == "4":
            print("Au revoir !")

        else:
            print("Choix invalide !")

main()
