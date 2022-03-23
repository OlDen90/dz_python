# не понял для чего нужен title. Возможно из-за
# этого всё задание выполнил не правильно.

class Stationery:
    # title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Маркер')

thing_1 = Stationery()
thing_1.draw()

thing_2 = Pen()
thing_2.draw()

thing_3 = Pencil()
thing_3.draw()

thing_4 = Handle()
thing_4.draw()