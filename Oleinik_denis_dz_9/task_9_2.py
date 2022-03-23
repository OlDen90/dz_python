# Не понял куда по заданию необходимо записать вес и толщину слоя асфальта.
# Записал туда же где и другие значения прописаны. На них защиту не делал.

# ВОПРОС! Как правильно (где, куда) в методах указывать значения данных - м, см, кг?

class Road:
    # length = 5000
    # width = 20

    def __init__(self):
        self._length = 5000
        self._width = 20
        self.mas_of_asphalt = 25
        self.depth = 5


a = Road()
print(f'{int((a._length * a._width * a.mas_of_asphalt * a.depth) / 1000)} т')
