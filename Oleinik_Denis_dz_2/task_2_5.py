praces = [57.8, 46.51, 97, 3.05, 103.20, 60.01, 73.89, 62.10, 1001.2, 1,
          0.52, 20.20, 34.65, 80, 75.80]
print('id before sorting', id(praces))

# point А
# сам решить не смог. Данный код списал с разбора ДЗ с целью разбора принципа работы
# for n in praces:
#     number = (f'{n:.2f}')
#     print((int(float(number))), 'руб', number[-2:], 'коп', end=',' )

# point B
praces.sort()
print('id after sorting', id(praces))
print(praces)

# point C
praces_s = sorted(praces, reverse=True)
print('id after reverse', id(praces_s))
print(praces_s)

# point D
# Variant 1
prases_5 = praces_s[0:5]
print('id prases_5 -', id(prases_5))
print(prases_5)

# Variant 2
praces_5_var_2 = sorted(praces, reverse=True)
praces_5_var_2 = praces_5_var_2[0:5]
print('id praces_5_var_2 -', id(praces_5_var_2))
print(praces_5_var_2)
