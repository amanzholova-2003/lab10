numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Проверяем, есть ли в списке хотя бы одно четное число
if any(num % 2 == 0 for num in numbers):
    print("В списке есть хотя бы одно четное число")
else:
    print("В списке нет четных чисел")

# Проверяем, все ли числа в списке меньше 11
if all(num < 11 for num in numbers):
    print("Все числа в списке меньше 11")
else:
    print("Не все числа в списке меньше 11")
