def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = []

    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result

def main():
    print("PART A - Transpose Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("Original Matrix:")
    print_matrix(matrix)

    print("Transposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    print("\nPART B - Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter first matrix:")
    matrix1 = read_matrix(rows, cols)

    print("Enter second matrix:")
    matrix2 = read_matrix(rows, cols)

    print("Sum of Matrices:")
    print_matrix(add_matrices(matrix1, matrix2))

    print("\nPART C - Multiply Two Matrices")
    rows1 = int(input("Enter rows for Matrix A: "))
    cols1 = int(input("Enter columns for Matrix A: "))
    matrix1 = read_matrix(rows1, cols1)

    rows2 = int(input("Enter rows for Matrix B: "))
    cols2 = int(input("Enter columns for Matrix B: "))

    if cols1 != rows2:
        print("Matrix multiplication is not possible.")
        return

    matrix2 = read_matrix(rows2, cols2)

    print("Product of Matrices:")
    print_matrix(multiply_matrices(matrix1, matrix2))

main()