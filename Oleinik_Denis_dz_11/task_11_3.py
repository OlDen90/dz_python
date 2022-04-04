# Не полное решение задачи

class MyOwnError(Exception):
    pass


inp_data = input('Введите число: ')

try:
    inp_data = int(inp_data)
#     print(f"Вы ввели число {inp_data}")
# except:
#     print("Вы ввели не число")
except (ValueError, MyOwnError) as err:
    print(err)
else:
    print(f"Вы ввели число {inp_data}")
