import time
import copy

class Cellule:
    """
    Classe representant une cellule dans la grille.

    Une cellule est caracterisee par ses coordonnees (i, j) et son statut d'occupation.

    >>> cell = Cellule(0, 0)
    >>> cell.i
    0
    >>> cell.j
    0
    >>> cell.occupee
    False
    """

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.occupee = False

class Grille:
    """
    Classe representant la grille du problème des N-Reines.

    La grille est constituee de cellules et permet de verifier si un coup est valide,
    de placer ou d'enlever une reine.

    >>> grille = Grille(4)
    >>> grille.possible(grille.grille[0][0])
    True
    >>> grille.possible(grille.grille[1][2])
    False
    >>> grille.placer_reine(grille.grille[1][1])
    >>> grille.grille[1][1].occupee
    True
    >>> grille.enlever_reine(grille.grille[1][1])
    >>> grille.grille[1][1].occupee
    False
    """

    def __init__(self, n):
        self.n = n
        self.grille = [[Cellule(i, j) for j in range(n)] for i in range(n)]

    def possible(self, cellule):
        """
        Vérifie si placer une reine dans la cellule est un coup valide.

        Un coup est valide si aucune reine n'est déjà placée sur la même ligne,
        colonne ou diagonale que la cellule.

        :param cellule: La cellule à vérifier.
        :return: True si le coup est valide, False sinon.
        """
        ligne = cellule.i
        colonne = cellule.j
        start_ligne = max(ligne - colonne, 0)
        start_colonne = max(colonne - ligne, 0)
        start_ligne_inv = min(ligne + colonne, self.n - 1)
        start_colonne_inv = max(colonne - (self.n - 1 - ligne), 0)

        for i in range(self.n):
            if self.grille[ligne][i].occupee or self.grille[i][colonne].occupee:
                return False
        
        verif = 0
        while start_ligne + verif < self.n and start_colonne + verif < self.n:
            if self.grille[start_ligne + verif][start_colonne + verif].occupee:
                return False
            verif += 1
    
        verif = 0
        while start_ligne_inv - verif >= 0 and start_colonne_inv + verif < self.n:
            if self.grille[start_ligne_inv - verif][start_colonne_inv + verif].occupee:
                return False
            verif += 1
    
        return True



    def placer_reine(self, cellule):
        """
        Place une reine dans la cellule specifiee.

        :param cellule: La cellule où placer la reine.
        """
        self.grille[cellule.i][cellule.j].occupee = True

    def enlever_reine(self, cellule):
        """
        Enlève une reine de la cellule specifiee.

        :param cellule: La cellule d'où enlever la reine.
        """
        self.grille[cellule.i][cellule.j].occupee = False

class Solution:
    """
    Classe representant une solution du problème des N-Reines.

    Une solution est simplement une grille où les reines sont placees de manière valide.

    >>> grille = Grille(4)
    >>> solution = Solution(grille)
    >>> solution.grille
    <__main__.Grille object at ...>
    """

    def __init__(self, grille):
        self.grille = grille

class Solveur:
    """
    Classe representant le solveur du problème des N-Reines.

    Le solveur utilise une approche de backtracking pour trouver toutes les solutions.

    >>> solveur = Solveur(4)
    >>> solveur.n
    4
    """

    def __init__(self, n):
        self.n = n
        self.solutions = []

    def backtracking(self, grille, ligne):
        """
        Fonction recursive pour le backtracking et la recherche de solutions.

        :param grille: La grille actuelle.
        :param ligne: La ligne actuelle à explorer.
        :return: True si une solution a ete trouvee, False sinon.
        """
        if ligne == self.n:
            self.ajouter_solution(grille)
            return True
        else:
            for j in range(self.n):
                if grille.possible(grille.grille[ligne][j]):
                    grille.placer_reine(grille.grille[ligne][j])
                    if self.backtracking(grille, ligne + 1):
                        grille.enlever_reine(grille.grille[ligne][j])
                    else:
                        grille.enlever_reine(grille.grille[ligne][j])
            return False

    def ajouter_solution(self, grille):
        """
        Fonction pour ajouter une solution au solveur.
        """
        
        self.solutions.append(Solution(copy.deepcopy(grille)))
    
    def resoudre(self):
        """
        Fonction principale pour resoudre le problème des N-Reines.
        """
        grille = Grille(self.n)
        self.backtracking(grille, 0)

    def afficher_toutes_les_solutions(self):
        """
        Affiche toutes les solutions trouvees par le solveur.
        """
        for i, solution in enumerate(self.solutions):
            print(f"Solution ", i + 1," :")
            self.afficher_solution(solution)

    def afficher_solution(self, solution):
        """
        Affiche une solution particulière.

        :param solution: La solution à afficher.
        """
        for i in range(self.n):
            for j in range(self.n):
                if solution.grille.grille[i][j].occupee:
                    print("| Q ", end="")
                else:
                    print("|   ", end="")
            print("|")
            for k in range(self.n):
                print("+---", end="")
            print("+")

def main():
    """
    Fonction principale pour resoudre et afficher les solutions du problème des N-Reines.
    """
    n = 8
    solveur = Solveur(n)

    print("Calcul des solutions...")

    debut = time.time()

    solveur.resoudre()

    fin = time.time()
    temps_cpu = fin - debut

    print(len(solveur.solutions),"solutions trouvees\nTemps CPU : ",temps_cpu," secondes")

    choix = ""
    while choix != "3":
        print("\n1. Afficher toutes les solutions\n2. Afficher une solution\n3. Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            solveur.afficher_toutes_les_solutions()
        elif choix == "2":
            num = int(input("Entrez le numero de la solution à afficher : "))
            if 1 <= num <= len(solveur.solutions):
                solveur.afficher_solution(solveur.solutions[num - 1])
            else:
                print("Numero de solution invalide !")
        elif choix == "3":
            print("Au revoir !")
        else:
            print("Choix invalide !")

if __name__ == "__main__":
    main()
