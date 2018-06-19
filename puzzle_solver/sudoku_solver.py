import csv

# i: row
# j: column


# Is given a list, and returns the missing sudoku numbers
def unseen_digits(seen_digits):
    unseen_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in seen_digits:
        if int(number) != 0:
            unseen_set.remove(int(number))
    return unseen_set



# Returns a list with the whole row
def return_row(sudoku, i):
    return sudoku[i]


# Returns a list with the whole column
def return_column(sudoku, j):
    column = []
    for item in sudoku:
        column.append(item[j])
    return column



# this has to check row, column and mini_box and determine whether there is only 1 possible value to put in the box
def single_solution(row, column, mini_box):

    r = unseen_digits(row)
    c = unseen_digits(column)
    b = unseen_digits(mini_box)

    # Finds the common missing elements of this row+column
    common = list(set(r) & set(c) & set(b))

    if len(common) == 1:
        return True, common[0]
    else:
        return False, False




# Returns 1 of the 9 possible mini boxes in the puzzle
def return_mini_box(sudoku, i, j):

    mini_box = []

    # Box 1
    if i < 3 and j < 3:
        for row in range(0, 3):
            for col in range(3):
                mini_box.append(sudoku[row][col])

    # Box 2
    if i < 3 and j < 6 and j > 3:
        for row in range(0, 3):
            for col in range(3, 6):
                mini_box.append(sudoku[row][col])

    # Box 3
    if i < 3 and j > 5:
        for row in range(0, 3):
            for col in range(6, 9):
                mini_box.append(sudoku[row][col])

    # Box 4
    if i < 6 and i > 2 and j < 3:
        for row in range(3, 6):
            for col in range(0, 3):
                mini_box.append(sudoku[row][col])

    # Box 5
    if i < 6 and i > 2 and j < 6 and j > 2:
        for row in range(3, 6):
            for col in range(3, 6):
                mini_box.append(sudoku[row][col])

    # Box 6
    if i < 6 and i > 2 and j > 5:
        for row in range(3, 6):
            for col in range(6, 9):
                mini_box.append(sudoku[row][col])

    # Box 7
    if i > 5 and j < 3:
        for row in range(6, 9):
            for col in range(0, 3):
                mini_box.append(sudoku[row][col])

    # Box 8
    if i > 5 and j > 2 and j < 6:
        for row in range(6, 9):
            for col in range(3, 6):
                mini_box.append(sudoku[row][col])

    # Box 9
    if i > 5 and j > 5:
        for row in range(6, 9):
            for col in range(6, 9):
                mini_box.append(sudoku[row][col])

    return mini_box


def write_results(sudoku, outfile):
    with open(outfile, "w") as sudoku_output:
        sudoku_writer = csv.writer(sudoku_output, delimiter=',')
        for row in sudoku:
            sudoku_writer.writerow(row)


def compare_sudokus(original_sudoku, solved_sudoku):
    new_numbers = 0
    return new_numbers


def solve_sudoku(infile, outfile):

    with open(infile, newline='') as sudoku_file:

        # Reads the CSV file and stores it as a 2D python list
        sudoku = list(csv.reader(sudoku_file, delimiter=','))

        for i, row in enumerate(sudoku):
            for j, number in enumerate(row):
                row = return_row(sudoku, i)
                column = return_column(sudoku, j)
                mini_box = return_mini_box(sudoku, i, j)

                # if there is a single solution and the box is empty
                if (single_solution(row, column, mini_box)[0] == True) and (number is "0"):
                    print("Found a single solution at row=", i+1, ", col=", j+1, sep="")
                    solution = single_solution(row, column, mini_box)[1]
                    print("Solution is:", solution, "\n")
                    sudoku[i][j] = solution

    write_results(sudoku, outfile)

    return 0


#print("The program needed", iteration(), "iterations.")


solve_sudoku(infile="solved_sudoku", outfile="solved_sudoku")

