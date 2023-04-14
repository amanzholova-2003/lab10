strings = input("Введите строку: ")  # считываем строку с клавиатуры

# создаем множество, чтобы получить только уникальные символы
chars = set(strings)

 # сортируем символы по алфавиту
sorted_chars = sorted(chars)

 # выводим результат на экран
print("Уникальные символы в строке: ", end="")
for char in sorted_chars:
     print(char, end="")
