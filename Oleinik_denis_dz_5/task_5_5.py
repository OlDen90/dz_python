src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Вариант на основе методички (написать с ноля сам не смог бы)
unique_src = set()
repeated_src = set()
for el in src:
    if el not in repeated_src:
        unique_src.add(el)
    else:
        unique_src.discard(el)
    repeated_src.add(el)
# print(unique_src)
print([el for el in src if el in unique_src])

# Вариант на основе вебинара (написать с ноля сам не смог бы)
unique_src = set()
repeated_src = set()
for el in src:
    if el in repeated_src:
        continue
    if el in unique_src:
        repeated_src.add(el)
        unique_src.discard(el)
        continue
    unique_src.add(el)
# print(unique_src)
print([el for el in src if el in unique_src])

