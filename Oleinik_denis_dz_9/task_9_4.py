# Код немного не доделал, так как запутался в задании.
# Не совсем пойму какой должен быть окончательный вывод
# информации, т.е. что задается и что в результате выводится.

# Подскажите, пожалуйста, как уйти от 39й строки,
# если её скрыть, возникает ошибка, если оставить,
# она дублируется с информацией в дочернем классе.

class Car:
    # speed = 60
    # color = black
    # name = some_car
    # is_police = PoliceCar

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.go()
        self.stop()
        self.turn_left()
        self.turn_right()
        self.show_speed()


    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} стоп")

    def turn_left(self):
        print(f"Машина {self.name} повернула налево")

    def turn_right(self):
        print(f"Машина {self.name} повернула направо")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч")


class TownCar(Car):
    def TownCar_method(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/ч")

class SportCar(Car):
    def SportCar_method(self):
        print(f'скорость авто {self.speed}')

class WorkCar(Car):
    def WorkCar_method(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/ч")

class PoliceCar(Car):
    def PoliceCar_method(self):
        print("На борту нашего автомобиля могла бы быть ваша реклама!")


auto_1 = TownCar(55, "black", "Audi")
auto_1.TownCar_method()

# auto_2 = SportCar(200, "white", "Lamba")
# auto_2.SportCar_method()

# auto_3 = Car(65, "yellow", "BMW")
# print('Цвет авто', auto_3.color)

