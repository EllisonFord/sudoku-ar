#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define UNASSIGNED 0
#define N 9
#define NN 81
using namespace std;


bool FindUnassignedLocation(int grid[N][N], int &row, int &col);
bool isSafe(int grid[N][N], int row, int col, int num);

// Converts the 2D input array to a 1D array
void matrix2array(int grid[N][N], int row_sudoku[NN])
{
    for (int q{0}; q < N; q++){
        for (int t{0}; t < N; t++){
            row_sudoku[q * N + t] = grid[q][t];
        }
    }
}

// Converts the 1D array to a 9x9 matrix
void array2matrix(int row_sudoku[NN], int grid[N][N])
{
    for (int q{0}; q < N; q++){
        for (int t{0}; t < N; t++){
            grid[q][t] = row_sudoku[q * N + t];
        }
    }
}


bool SolveSudoku(int grid[N][N])
{
    int row, col;
    if (!FindUnassignedLocation(grid, row, col))
        return true;
    for (int num = 1; num <= N; num++)
    {
        if (isSafe(grid, row, col, num))
        {
            grid[row][col] = num;
            if (SolveSudoku(grid))
                return true;
            grid[row][col] = UNASSIGNED;
        }
    }
    return false;
}

/* Searches the grid to find an entry that is still unassigned. */
bool FindUnassignedLocation(int grid[N][N], int &row, int &col)
{
    for (row = 0; row < N; row++)
        for (col = 0; col < N; col++)
            if (grid[row][col] == UNASSIGNED)
                return true;
    return false;
}

/* Returns whether any assigned entry n the specified row matches
 the given number. */
bool UsedInRow(int grid[N][N], int row, int num)
{
    for (int col = 0; col < N; col++)
        if (grid[row][col] == num)
            return true;
    return false;
}

/* Returns whether any assigned entry in the specified column matches
 the given number. */
bool UsedInCol(int grid[N][N], int col, int num)
{
    for (int row = 0; row < N; row++)
        if (grid[row][col] == num)
            return true;
    return false;
}

/* Returns whether any assigned entry within the specified 3x3 box matches
 the given number. */
bool UsedInBox(int grid[N][N], int boxStartRow, int boxStartCol, int num)
{
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return true;
    return false;
}

/* Returns whether it will be legal to assign num to the given row,col location.
 */
bool isSafe(int grid[N][N], int row, int col, int num)
{
    return !UsedInRow(grid, row, num) && !UsedInCol(grid, col, num) &&
           !UsedInBox(grid, row - row % 3 , col - col % 3, num);
}

void printGrid(int grid[N][N])
{
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
            cout<<grid[row][col]<<"  ";
        cout<<endl;
    }
}

void print1D(int input[NN])
{
    cout << "Sudoku in Row Major: ";
    for (int i{0}; i < NN; i += 1) {
        cout << input[i];
    }
    cout << endl;
}

/*
void set_difference(const int& a[NN], const int& b[NN], int& c[NN]){

    set_difference(begin(a), end(a),
                   begin(b), end(b),
                   back_inserter(c));

}
*/

void set_difference(const int& unsolved[NN], const int& solved[NN], int& difference[NN])
{

    array<int, NN> difference = unsolved;

    for (int i = 0; i < NN; i += 1){
        if (unsolved[i] == solved[i]){
            difference[i] = 0;
        }
    }



}


int main()
{
    int input_grid[N][N] = {
            {3, 0, 6, 5, 0, 8, 4, 0, 0},
            {5, 2, 0, 0, 0, 0, 0, 0, 0},
            {0, 8, 7, 0, 0, 0, 0, 3, 1},
            {0, 0, 3, 0, 1, 0, 0, 8, 0},
            {9, 0, 0, 8, 6, 3, 0, 0, 5},
            {0, 5, 0, 0, 9, 0, 6, 0, 0},
            {1, 3, 0, 0, 0, 0, 2, 5, 0},
            {0, 0, 0, 0, 0, 0, 0, 7, 4},
            {0, 0, 5, 2, 0, 6, 3, 0, 0}};


    // Turn into row
    int input_as_row[NN];
    matrix2array(input_grid, input_as_row);

    cout << endl; printGrid(input_grid);

    cout << endl; print1D(input_as_row); cout << "\n\n\n";

    if (SolveSudoku(input_grid))
    {
        // solved Sudoku
        printGrid(input_grid);

        int solved_as_row[NN];
        matrix2array(input_grid, solved_as_row);

        cout << endl; print1D(solved_as_row); cout << endl;


        int difference_row[NN];

        set_difference(input_as_row, solved_as_row, difference_row);

        print1D(difference_row);

    }

    else
        cout << "No solution exists" << endl;

}






