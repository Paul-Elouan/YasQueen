#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define N 3

typedef int grille[N][N];

bool possible(grille g, int numCase);

int main()
{
    grille g;

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
    int verifFin = (numCase + 1) / N;

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