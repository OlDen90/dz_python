cube = []

for i in range(1, 1001):
    if i % 2 != 0:
        cube.append(i ** 3)     # про append подсмотрел в разборе ДЗ в вэбинаре 2
        # print(cube)
for index, cube_ in enumerate(cube):
    sum = 0
    while cube_:  # не понимаю как это всё работает и что делать дальше.
        sum += cube_ % 10
        cube_ = cube_ // 10
    print(sum)
# решение с 7 по 12 строки находил в интернете, немного переделал относительно разбора ДЗ
# в вэбинаре 2, но сам додуматься как это работает и что делать дальше - не смог. Передирать не стал.
