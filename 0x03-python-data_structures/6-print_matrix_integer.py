def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)  # length of the matrix
    columns = len(matrix[0])  # length of the first row in matrix

    if matrix == [[]]:
        print()

    for n in range(rows):
        for m in range(columns):
            if m == columns - 1:
                print("{:d}".format(matrix[n][m]))
            else:
                print("{:d}".format(matrix[n][m]), end=" ")
