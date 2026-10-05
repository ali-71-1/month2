# Car — родительский класс (суперкласс): в нем описано общее для машин.
class Car:
    def __init__(self, wheels, color, marka):
        # self.wheels, self.color, self.marka — атрибуты объекта
        self.wheels = wheels
        self.color = color
        self.marka = marka
        self.fined = False

    # Методы Car доступны объектам Car и его дочерних классов.
    def change_color(self, new_color):
        # меняем атрибут color у конкретного объекта
        self.color = new_color

    def is_fined(self):
        return self.fined

    def drive_to(self, destination):
        # self.marka — обращение к атрибуту внутри метода
        if self.is_fined():
            print("Машина на штраф-стоянке")
            return
        print(f"Машина марки {self.marka} едет в {destination}")

# ElectricCar расширяет Car: наследует его атрибуты и методы, а также добавляет
# собственный атрибут battery и метод charge.
class ElectricCar(Car):
    def __init__(self, wheels, color, marka):
        # super() позволяет обратиться к реализации родительского класса Car.
        # Здесь super().__init__(...) запускает родительский конструктор,
        # чтобы создать общие атрибуты машины без повторения кода.
        super().__init__(wheels, color, marka)
        # Добавляем атрибут, который есть только у электромобиля.
        self.battery = 0

    def charge(self):
        # При зарядке добавляем 10%; ограничиваем значение сверху 100%.
        self.battery += 10
        if self.battery > 100:
            self.battery = 100

    def drive_to(self, destination):
        # Это переопределение (замена реализации) метода drive_to из Car:
        # у электромобиля перед поездкой нужно проверить заряд батареи.
        if self.battery <= 0:
            print("Не хватает заряда")
            return
        # super().drive_to(...) вызывает исходный метод родителя Car,
        # сохраняя его логику (например, проверку штрафа). Затем тратим заряд.
        super().drive_to(destination)
        self.battery -= 20


# SportCar тоже наследует Car: получает его конструктор и методы без повторного кода.
class SportCar(Car):
    pass

# Создаем электромобиль; его конструктор также создает общие атрибуты Car.
my_car1 = ElectricCar(4, "black", "Tesla")
print(my_car1.marka, my_car1.wheels, my_car1.fined, my_car1.battery)
my_car1.fined = True
my_car1.drive_to("Каракол")
my_car1.charge()
my_car1.charge()
my_car1.drive_to("Каракол")
my_car1.fined = False
my_car1.charge()
my_car1.charge()

print(type(my_car1))
# isinstance проверяет, относится ли объект к классу или его родительскому классу.
print(isinstance(my_car1, Car))
my_car2 = Car(4, "silver", "Toyota")
my_car3 = SportCar(4, "red", "Mercedes")

# В списке объекты разных классов. Один и тот же вызов drive_to ниже
# выбирает реализацию по типу объекта: у ElectricCar метод переопределен,
# а Car и SportCar используют унаследованный метод Car. Это полиморфизм.
vehicles = [my_car1, my_car2, my_car3]
for v in vehicles:
    v.drive_to("Кара-Балта")

