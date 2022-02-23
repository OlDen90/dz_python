def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


odd_to_15 = odd_nums(15)

for next_odd in odd_to_15:
    print(next_odd)

# print(*odd_to_15)     # 1 3 5 7 9 11 13 15

# print(next(odd_to_15))  # 1
# print(next(odd_to_15))  # 3
# print(next(odd_to_15))  # 5
# print(next(odd_to_15))  # 7
# print(next(odd_to_15))  # 9
# print(next(odd_to_15))  # 11
# print(next(odd_to_15))  # 13
# print(next(odd_to_15))  # 15
