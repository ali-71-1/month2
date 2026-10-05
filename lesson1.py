class Car:
    # конструктор
    # __init__ вызывается автоматически при создании объекта Car(...)
    # self — конкретный создаваемый объект
    def __init__(self, wheels, color, marka):
        # self.wheels, self.color, self.marka — атрибуты объекта
        self.wheels = wheels
        self.color = color
        self.marka = marka

    # метод — функция внутри класса, всегда принимает self
    def change_color(self, new_color):
        # меняем атрибут color у конкретного объекта
        self.color = new_color

    def drive_to(self, destination):
        # self.marka — обращение к атрибуту внутри метода
        print(f"Машина марки {self.marka} едет в {destination}")


# создание объекта путем "вызова" класса — вызывает __init__ автоматически
my_car1 = Car(4, "black", "Honda")
my_car2 = Car(4, "silver", "Toyota")
# без специального метода Python выводит служебное представление объекта
print(my_car1, my_car2)
# обращение к атрибутам/свойствам объекта через точку
print(f"wheels: {my_car1.wheels}, color: {my_car1.color}, marka {my_car1.marka}")
print(f"wheels: {my_car2.wheels}, color: {my_car2.color}, marka {my_car2.marka}")
# атрибут объекта можно изменить напрямую после создания
my_car2.color = "white"
print(my_car2.color, my_car2.marka)
# а можно через метод — так обычно правильнее
my_car1.change_color("silver")
print(my_car1.color, my_car1.marka)
# вызов метода: объект.my_method(аргументы)
my_car2.drive_to("Кант")

