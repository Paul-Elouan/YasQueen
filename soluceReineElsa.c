#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define N 8

typedef int grille[N][N];

bool possible(grille g, int ligne, int colonne);
bool backtracking(grille g, int numCase, int nbReines);
void afficherGrille(grille g);
void initGrille(grille g);


int main()
{
    grille g;
    int numCase = 0;
    initGrille(g);
    afficherGrille(g);
    backtracking(g, numCase, N);
    afficherGrille(g);
    return EXIT_SUCCESS;
}

/* fonction qui vérifie si une on peut placer une dame dans l'échiquier. 
Une dame est représenter par un 1 et une case vide par un 0. On doit vérifier si 
il est possible de placer la dame dans la case  */
bool possible(grille g, int ligne, int colonne)
{
    int startLigne, startColonne;
    // vérifie si le chiffre 1 est présent dans la ligne, la colonne ou les diagonales
    for (int i = 0; i < N; i++)
    {
        if (g[ligne][i] == 1 || g[i][colonne] == 1)
        {
            return false;
        }
    }
    // verification des diagonales
    int verifFin = (ligne + 1) / N;
    for (int i = 0; i < verifFin; i++)
    {
        if (ligne - i < 0)
        {
            startLigne = 0;
        }
        else
        {
            startLigne = ligne - i;
        }
    }
    for (int i = 0; i < verifFin; i++)
    {
        if (colonne - i < 0)
        {
            startColonne = 0;
        }
        else
        {
            startColonne = colonne - i;
        }
        if (g[startLigne + i][startColonne + i] == 1)
        {
            return false;
        }
    }
    return true;
}

void initGrille(grille g)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            g[i][j] = 0;
        }
    }
}

bool backtracking(grille g, int numCase, int nbReines)
{
    int ligne, colonne;

    if (numCase == N * N || nbReines == 0)
    {
        return true;
    }
    else
    {
        ligne = numCase / N;
        colonne = numCase % N;
        
        if (g[ligne][colonne]!=0)
        {
            return backtracking(g, numCase + 1, nbReines);
        }
        else
        {
            for (int i = 1; i <= N; i++)
            {
                g[ligne][colonne] = 1;
                if (possible(g, ligne, colonne))
                {
                    if (backtracking(g, numCase + 1, nbReines - 1))
                    {
                        nbReines--;
                        return true;
                    }
                }
            }
            g[ligne][colonne] = 0;
            return false;
        }
    }
}

void afficherGrille(grille g)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d ", g[i][j]);
        }
        printf("\n");
    }
}