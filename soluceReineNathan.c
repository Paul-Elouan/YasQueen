#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define N 8

typedef int grille[N][N];

bool possible(grille g, int numCase);
bool backtracking(grille g, int numCase, int nbDames);
void afficherGrille(grille g);
void initGrille(grille g);

int main()
{
    grille g;
    initGrille(g);

    backtracking(g, 0, 0);

    afficherGrille(g);

    return EXIT_SUCCESS;
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

bool possible(grille g, int numCase)
{
    int ligne = numCase / N;
    int colonne = numCase % N;
    int startLigne, startColonne, startLigneInv, startColonneInv;
    // vérifie si le chiffre 1 est présent dans la ligne, la colonne ou les diagonales
    for (int i = 0; i < N; i++)
    {
        if (g[ligne][i] == 1 || g[i][colonne] == 1)
        {
            return false;
        }
    }
    // verification des diagonales
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

    if (ligne + colonne >= N)
    {
        startLigneInv = N - 1;
    }
    else
    {
        startLigneInv = ligne + colonne;
    }

    if (colonne - ((N - 1) - ligne) < 0)
    {
        startColonneInv = 0;
    }
    else
    {
        startColonneInv = colonne - ((N - 1) - ligne);
    }

    int verif = 0;

    // Diagonale haut gauche / bas droite
    while (startLigne + verif < N && startColonne + verif < N)
    {
        if (g[startLigne + verif][startColonne + verif] == 1)
        {
            return false;
        }
        verif++;
    }

    verif = 0;

    // Diagonale bas gauche / haut droite
    while (startLigneInv - verif >= 0 && startColonneInv + verif < N)
    {
        if (g[startLigneInv - verif][startColonneInv + verif] == 1)
        {
            return false;
        }
        verif++;
    }
    return true;
}

bool backtracking(grille g, int numCase, int nbDames)
{
    if (nbDames == N)
    {
        return true;
    }
    else
    {
        for (int i = 0; i < (N * N) - numCase - 1; i++)
        {
            if (possible(g, numCase + i))
            {
                int ligne = (numCase + i) / N;
                int colonne = (numCase + i) % N;
                g[ligne][colonne] = 1;
                if (backtracking(g, numCase + i + 1, nbDames + 1))
                {
                    return true;
                }
                else
                {
                    g[ligne][colonne] = 0;
                }
            }
        }
        return false;
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