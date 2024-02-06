#define N 3
#define GRID_SIZE 8
typedef int grille[N][N];

void fillRandomGrid(grille grid) {
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int j = 0; j < GRID_SIZE; j++) {
            grid[i][j] = rand() % 2;
        }
    }
}

void affichage(grille grid) {
    printf("+---------+---------+---------+---------+---------+---------+---------+---------+\n");
    for (int i = 0; i < GRID_SIZE; i++) {
        for (int k = 0; k < N; k++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (grid[i][j] == 1) {
                    switch (k)
                    {
                    case 0:
                        printf("|   _O_   ");
                        break;
                    case 1:
                        printf("|   \ /   ");
                        break;
                    case 2:
                        printf("|   /_\\   ");
                        break;

                    default:
                        break;
                    }
                }

                else {
                    printf("|         ");
                }
            }
            printf("|\n");
        }
        printf("+---------+---------+---------+---------+---------+---------+---------+---------+\n");
    }
}