def rotate_matrix_clockwise(matrix):
    """
    Функция, которая поворачивает матрицу на 90 градусов по часовой стрелке
    :param matrix: исходная матрица (список списков)
    :return: повернутая матрица (список списков)
    """
    # используем функцию zip() и reversed() для получения столбцов матрицы
    columns = [list(reversed(col)) for col in zip(*matrix)]
    # возвращаем транспонированную матрицу, которая является результатом поворота на 90 градусов
    return [list(row) for row in zip(*columns)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Вызывваем функцию 
rotated_matrix = rotate_matrix_clockwise(matrix)
print(rotated_matrix)
