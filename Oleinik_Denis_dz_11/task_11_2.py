class MyOwnError(Exception):
    pass


inp_data_1 = input('Введите первое число: ')
inp_data_2 = input('Введите второе число: ')

try:
    data = int(inp_data_1)/int(inp_data_2)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except (ValueError, MyOwnError) as err:
    print(err)
else:
    print(f"Ваш результат {data}")
