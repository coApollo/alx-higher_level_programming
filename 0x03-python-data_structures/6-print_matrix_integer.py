#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (not matrix or not any(matrix)):
        return
    outer = len(matrix)
    for i in range(outer):
        inner = len(matrix[i])
        for j in range(inner):
            print("{:d}".format(matrix[i][j]), end='')
            if (j < inner - 1):
                print(' ', end='')
        print()
    return (None)
