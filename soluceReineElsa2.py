import time

class Graphe(object):

    def __init__(self, graphe_dict=None):
        if graphe_dict is None:
            graphe_dict = dict()
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        return self._graphe_dict[sommet]

    def all_sommets(self):
        return self._graphe_dict.keys()

    def all_aretes(self):
        return self.__list_aretes()

    def add_sommet(self, sommet):
        if sommet not in self._graphe_dict.keys():
            self._graphe_dict[sommet] = []

    def add_arete(self, arete):
        self._graphe_dict[arete[0]].append(arete[1])

    def __list_aretes(self):
        return [(sommet, voisin) for sommet in self._graphe_dict.keys() for voisin in self._graphe_dict[sommet]]

    def __iter__(self):
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        return next(self._iter_obj)

    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict.keys():
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res

    def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
        if chain is None:
            chain = []
        chain.append(sommet_dep)
        if sommet_dep == sommet_arr:
            return chain
        for voisin in self.aretes(sommet_dep):
            if voisin not in chain:
                next_chain = self.trouve_chaine(voisin, sommet_arr, chain[:])
                if next_chain:
                    return next_chain
        return None

    def trouve_tous_chemins(self, sommet_dep, sommet_arr, chem=[]):
        chem.append(sommet_dep)
        if sommet_dep == sommet_arr:
            return [chem]
        
        chemins =[]

        for voisin in self.aretes(sommet_dep):
            if voisin not in chem:
                nouveaux_chemins = self.trouve_tous_chemins(voisin, sommet_arr, chem[:])
                for nouveau_chemin in nouveaux_chemins:
                    chemins.append(nouveau_chemin)
        return chemins


def resoudre_probleme_n_reines(n):
    graphe = Graphe()
    for i in range(n):
        graphe.add_sommet(i)
    for i in range(n):
        for j in range(i + 1, n):
            graphe.add_arete((i, j))
            graphe.add_arete((j, i))
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                graphe.add_arete((i, j))
                graphe.add_arete((i, k))
                graphe.add_arete((j, k))
    return graphe


def affiche_solutions_probleme_reines(graphe, sommet_dep, sommet_arr):
    sommets = list(graphe.all_sommets())
    chemins = graphe.trouve_tous_chemins(sommet_dep, sommet_arr)
    nbsolutions = len(chemins)

    print(nbsolutions, "solutions trouvée(s) !\n")

    choix = 0
    while choix != 3:
        choix = int(input("Voulez-vous afficher toutes les solutions ? (1) \nVoulez-vous afficher une solution particulière ? (2) \nVoulez-vous quitter ? (3) \n"))
        
        if choix == 1:
            print(graphe.__str__())
        elif choix == 2:
            print("Veuillez entrer le nombre de la solution que vous voulez afficher :")
            choix_solution = int(input())
            for j in range(nbsolutions):
                if j == choix_solution-1:
                    print(chemins[j])
                    print("\n")
                    return
        elif choix == 3:
            print("Au revoir !")
            break
        else:
            print("Veuillez entrer un nombre compris entre 1 et 3")
            continue

        print("\n")


if __name__ == "__main__":
    n = int(input("Veuillez entrer le nombre de reines :"))
    start = time.time()
    graphe = resoudre_probleme_n_reines(n)
    affiche_solutions_probleme_reines(graphe, 0, n-1)
    end = time.time()
    tot = end - start
    print(tot)



