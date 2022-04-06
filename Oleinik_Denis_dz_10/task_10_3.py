# Задача без make_order

class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return f"{self.numbers}"

    def __add__(self, other):
        print("Сложение:")
        return Cell(self.numbers + other.numbers)

    def __sub__(self, other):
        print("Вычитание:")
        if self.numbers < other.numbers:
            return "Вычитание невозможно, ячеек в первой клетке меньше чем во второй!"
        else:
            return Cell(self.numbers - other.numbers)

    def __mul__(self, other):
        print("Умножение:")
        return Cell(self.numbers * other.numbers)

    def __floordiv__(self, other):
        print("Деление:")
        return Cell(self.numbers / other.numbers)


cell_1 = Cell(10)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
