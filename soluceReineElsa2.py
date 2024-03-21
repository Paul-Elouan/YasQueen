import time
class Graphe:
    def __init__(self, num_reines):
        self.num_reines = num_reines
        graphe_dict = dict()
        self.graphe = graphe_dict


    def ajouter_arete(self, u, v):
        if u in self.graphe:
            self.graphe[u].append(v)
        else:
            self.graphe[u] = [v]

    def __str__(self):
       res = "sommets: "
       for k in self.graphe.keys():
           res += str(k) + " "
       res += "\naretes: "
       for arete in self.__list_aretes():
           res += str(arete) + " "
       return res
    
    def __list_aretes(self):
        """ Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
            avec un (boucle) ou deux sommets.
        """
        return [arete for arete in self.graphe.values() for arete in arete]
    
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
        """construit le graphe avec le nombre reines en paramètres"""
        for i in range(num_reines):
            

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
    print(graphe.__str__())
    end = time.time()
    tmps_cpu = end - begin
    print("Temps CPU:", tmps_cpu)
    
    #solutions = graphe.resoudre_n_reines()
    #print("Nombre de solutions trouvées:", len(solutions))
    #afficher_solution(solutions, num_reines)


if __name__ == "__main__":
    main()
