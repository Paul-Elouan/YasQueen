import random

N = 8

def random_grid(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = 0
    for i in range(N):
        ligne = random.randint(0, N - 1)
        colonne = random.randint(0, N - 1)
        grid[ligne][colonne] = 1
    return grid


def affichage(grid):
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

def affichageMinimaliste(grid):
    for k in range(N):
        print("+---", end="")
    print("+")
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                print("| Q ", end="")
            else:
                print("|   ", end="")
        print("|")
        for k in range(N):
            print("+---", end="")
        print("+")

grid = [[0] * N for i in range(N)]
random_grid(grid)
affichage(grid)
affichageMinimaliste(grid)