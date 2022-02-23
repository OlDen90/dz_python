odd_to_15 = (number for number in range(1, 15 + 1, 2))
print(*odd_to_15)


# или


n = 15
# n = int(input('Введите число: '))     # Как вариант


odd_to_15_var_2 = (number_2 for number_2 in range(1, n + 1, 2))
print(*odd_to_15_var_2)

