#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define N 3

typedef int grille[N][N];

bool possible(grille g, int numCase);
bool backtracking(grille g, int numCase);
void afficherGrille(grille g);
void initGrille(grille g);


int main()
{
    grille g;
    int numCase = 0;
    initGrille(g);
    afficherGrille(g);
    backtracking(g, numCase);
    afficherGrille(g);
    return EXIT_SUCCESS;
}

bool possible(grille g, int numCase)
{
    int ligne = numCase / N;
    int colonne = numCase % N;
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
    int verifFin = (numCase + 1) % N;

    if (ligne - colonne < 0)
    {
        startLigne = 0;
    }
    else
    {
        startLigne = ligne - colonne;
    }

    if (colonne - ligne < 0)
    {
        startColonne = 0;
    }
    else
    {
        startColonne = colonne - ligne;
    }

    for (int verif = 0; verif < verifFin; verif++)
    {
        if (g[startLigne + verif][startColonne + verif] == 1)
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

bool backtracking(grille g, int numCase)
{
    int ligne, colonne;

    if (numCase == N * N)
    {
        return true;
    }
    else
    {
        ligne = numCase / N;
        colonne = numCase % N;
        
        if (g[ligne][colonne]!=0)
        {
            return backtracking(g, numCase + 1);
        }
        else
        {
            for (int i = 1; i <= N; i++)
            {
                g[ligne][colonne] = 1;
                if (possible(g, numCase))
                {
                    if (backtracking(g, numCase + 1))
                    {
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