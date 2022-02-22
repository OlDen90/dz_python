def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


odd_to_15 = odd_nums(15)

# print(*odd_to_15)     # 1 3 5 7 9 11 13 15

print(next(odd_to_15))  # 1
print(next(odd_to_15))  # 3
print(next(odd_to_15))  # 5
print(next(odd_to_15))  # 7
print(next(odd_to_15))  # 9
print(next(odd_to_15))  # 11
print(next(odd_to_15))  # 13
print(next(odd_to_15))  # 15

# Принцип работы вроде понял, но как правильно подписывать/именовать после for, т.е. что
# написать вместо num чтобы код был хорошо читаем, другими словами, что есть num?
# Аналогичный вопрос и к task_5_2
