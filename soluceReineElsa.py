import time
import copy

class Cellule:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.occuped = False

class Grille:
    def __init__(self, n):
        self.n = n
        self.grid = [[Cellule(i, j) for j in range(n)] for i in range(n)]

    def is_valid_move(self, cell):
        for i in range(self.n):
            if self.grid[cell.i][i].occuped or self.grid[i][cell.j].occuped:
                return False
        
        for i, j in zip(range(cell.i, -1, -1), range(cell.j, -1, -1)):
            if self.grid[i][j].occuped:
                return False
        
        for i, j in zip(range(cell.i, self.n, 1), range(cell.j, -1, -1)):
            if self.grid[i][j].occuped:
                return False
        
        return True

    def place_queen(self, cell):
        self.grid[cell.i][cell.j].occuped = True

    def remove_queen(self, cell):
        self.grid[cell.i][cell.j].occuped = False

class Solution:
    def __init__(self, grid):
        self.grid = grid

class Solver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def backtracking(self, grid, row):
        if row == self.n:
            self.solutions.append(Solution(copy.deepcopy(grid)))
            return True
        else:
            for j in range(self.n):
                if grid.is_valid_move(grid.grid[row][j]):
                    grid.place_queen(grid.grid[row][j])
                    if self.backtracking(grid, row + 1):
                        grid.remove_queen(grid.grid[row][j])
                    else:
                        grid.remove_queen(grid.grid[row][j])
            return False

    def solve(self):
        grid = Grille(self.n)
        self.backtracking(grid, 0)

    def display_all_solutions(self):
        for i, solution in enumerate(self.solutions):
            print(f"Solution {i + 1}:")
            self.display_solution(solution)

    def display_solution(self, solution):
        for i in range(self.n):
            for j in range(self.n):
                if solution.grid.grid[i][j].occuped:
                    print("| Q ", end="")
                else:
                    print("|   ", end="")
            print("|")
            for k in range(self.n):
                print("+---", end="")
            print("+")

def main():
    n = 8
    solver = Solver(n)

    print("Calcul des solutions...")

    begin = time.time()

    solver.solve()

    end = time.time()
    cpu_time = end - begin

    print(f"{len(solver.solutions)} solutions trouvées\nTemps CPU : {cpu_time:.3f} secondes")

    choice = ""
    while choice != "3":
        print("\n1. Afficher toutes les solutions\n2. Afficher une solution\n3. Quitter")
        choice = input("Entrez votre choix : ")

        if choice == "1":
            solver.display_all_solutions()
        elif choice == "2":
            num = int(input("Entrez le numéro de la solution à afficher : "))
            if 1 <= num <= len(solver.solutions):
                solver.display_solution(solver.solutions[num - 1])
            else:
                print("Numéro de solution invalide !")
        elif choice == "3":
            print("Au revoir !")
        else:
            print("Choix invalide !")

if __name__ == "__main__":
    main()
