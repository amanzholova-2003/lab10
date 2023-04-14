def matrix_operation(matrix1, matrix2, operation):
    # проверяем размерности матриц
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    # создаем результирующую матрицу
    result_matrix = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    # выполняем операцию
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if operation == '+':
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            elif operation == '-':
                result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            elif operation == '*':
                result_matrix[i][j] = matrix1[i][j] * matrix2[i][j]
    return result_matrix
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_matrix = matrix_operation(matrix1, matrix2, '+')
print(result_matrix)  # [[6, 8], [10, 12]]

result_matrix = matrix_operation(matrix1, matrix2, '-')
print(result_matrix)  # [[-4, -4], [-4, -4]]

result_matrix = matrix_operation(matrix1, matrix2, '*')
print(result_matrix)  # [[5, 12], [21, 32]]
