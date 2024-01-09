#!/usr/bin/python3
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n_string = sys.argv[1]
    try:
        n = int(n_string)
    except ValueError:
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    puzzle_solver(n)


def puzzle_solver(n):

    iterations = 1
    first_queen_pos = 0

    while n - iterations >= 2:
        first_queen_pos += 1
        iterations += 1
        chessboard = []
        possible_positions = []

        for i in range(n):
            chessboard.append([])
            for j in range(n):
                chessboard[i].append(1)

        chessboard = clear_path_for_queen(chessboard, [0, first_queen_pos])
        possible_positions.append([0, first_queen_pos])

        for i in range(n):
            for j in range(n):
                if chessboard[i][j] == 1:
                    possible_positions.append([i, j]) if [i, j] not in \
                                                possible_positions else None
                    chessboard = clear_path_for_queen(chessboard, [i, j])

        print(possible_positions)


def clear_path_for_queen(chessboard, pos):

    n = len(chessboard[0])

    for i in range(0, n):
        if pos != [pos[0], i]:
            chessboard[pos[0]][i] *= 0

    #  Clear the vertical places
    for i in range(0, n):
        if pos != [i, pos[1]]:
            chessboard[i][pos[1]] *= 0

    #  Clear the diagonals
    i = pos[0] - 1
    j = pos[1] - 1

    #  Clear the left corner diagonals
    while i > -1 and j > -1:
        chessboard[i][j] *= 0
        i -= 1
        j -= 1

    i = pos[0] + 1
    j = pos[1] - 1

    #  Clear the right corner diagonals
    while i < n and j > -1:
        chessboard[i][j] *= 0
        i += 1
        j -= 1

    i = pos[0] + 1
    j = pos[1] + 1

    #  Clear the right bottom diagonals
    while i < n and j < n:
        chessboard[i][j] *= 0
        i += 1
        j += 1

    i = pos[0] - 1
    j = pos[1] + 1

    #  Clear the left bottom diagonals
    while i > -1 and j < n:
        chessboard[i][j] *= 0
        i -= 1
        j += 1

    return chessboard


if __name__ == "__main__":
    main()
