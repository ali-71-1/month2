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
        """метод для проверки свойства"""
        return self.fined

    def drive_to(self, destination):
        # self.marka — обращение к атрибуту внутри метода
        if self.is_fined():
            print("Машина на штраф-стоянке")
            return
        print(f"Машина марки {self.marka} едет в {destination}")


if __name__ == "__main__":
    # Создаем два независимых объекта одного класса; для каждого вызывается __init__.
    my_car1 = Car(4, "black", "Honda")
    my_car2 = Car(4, "silver", "Toyota")
    # без специального метода Python выводит служебное представление объекта
    print(my_car1, my_car2)
    # Читаем атрибуты конкретных объектов через точку: объект.атрибут.
    print(f"wheels: {my_car1.wheels}, color: {my_car1.color}, marka {my_car1.marka}")
    print(f"wheels: {my_car2.wheels}, color: {my_car2.color}, marka {my_car2.marka}")
    # атрибут объекта можно изменить напрямую после создания
    my_car2.color = "white"
    print(my_car2.color, my_car2.marka)
    # Метод меняет атрибут выбранного объекта; self внутри метода указывает на него.
    my_car1.change_color("silver")
    print(my_car1.color, my_car1.marka)
    # Вызов метода: объект.имя_метода(аргументы). self указывать не нужно — Python передаст его сам.
    print(f"Машина {my_car2.marka} оштрафована: {'да' if my_car2.is_fined() else 'нет'}")
    my_car2.drive_to("Кант")
    print(type("fsdfsd"), type(123), type(my_car2))
    my_car2.horse_power = 100  # добавляем динамический атрибут - Python позволяет так делать, но лучше не делать так, приведет к ошибкам
    print(my_car2.horse_power)
    # print(my_car1.horse_power)