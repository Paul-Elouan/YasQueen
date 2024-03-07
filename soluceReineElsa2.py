import time
class Graphe:
    def __init__(self, num_reines):
        self.num_reines = num_reines
        self.graphe = {}

    def ajouter_arete(self, u, v):
        if u in self.graphe:
            self.graphe[u].append(v)
        else:
            self.graphe[u] = [v]

    def resoudre_n_reines(self):
        solutions = []
        visites = set()

        def dfs(noeud, chemin):
            visites.add(noeud)
            chemin.append(noeud)

            if len(chemin) == self.num_reines:
                solutions.append(chemin[:])
            else:
                for voisin in self.graphe.get(noeud, []):
                    if voisin not in visites:
                        dfs(voisin, chemin)

            chemin.pop()
            visites.remove(noeud)

        for noeud in self.graphe.keys():
            dfs(noeud, [])

        return solutions


def est_securitaire(plateau, ligne, colonne):
    # Vérifie si une reine peut être placée sur la case (ligne, colonne)
    # en vérifiant les lignes, les colonnes et les diagonales
    for i in range(ligne):
        if plateau[i] == colonne or \
           plateau[i] - i == colonne - ligne or \
           plateau[i] + i == colonne + ligne:
            return False
    return True

def construire_graphe(graphe, plateau, ligne, num_reines):
        if ligne == num_reines:
            return

        for colonne in range(num_reines):
            if est_securitaire(plateau, ligne, colonne):
                plateau[ligne] = colonne
                if ligne > 0:
                    ligne_precedente = ligne - 1
                    colonne_precedente = plateau[ligne_precedente]
                    noeud_precedent = ligne_precedente * num_reines + colonne_precedente
                    noeud_actuel = ligne * num_reines + colonne
                    graphe.ajouter_arete(noeud_precedent, noeud_actuel)
                construire_graphe(graphe, plateau, ligne + 1, num_reines)

def construire_graphe_reines(num_reines):
    graphe = Graphe(num_reines)
    plateau = [-1] * num_reines

    construire_graphe(graphe, plateau, 0, num_reines)
    return graphe


def afficher_solution(solution, num_reines):
    for plateau in solution:
        for ligne in range(num_reines):
            ligne_str = ['Q' if i == plateau[ligne] else '.' for i in range(num_reines)]
            print(' '.join(ligne_str))
        print()


def main():
    num_reines = 8
    print("Calcul des solutions...")

    begin = time.time()
    
    graphe = construire_graphe_reines(num_reines)
    
    end = time.time()
    tmps_cpu = end - begin
    print("Temps CPU:", tmps_cpu)
    
    solutions = graphe.resoudre_n_reines()
    print("Nombre de solutions trouvées:", len(solutions))
    afficher_solution(solutions, num_reines)


if __name__ == "__main__":
    main()
