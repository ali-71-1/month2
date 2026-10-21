# Инкапсуляция: данные и методы, которые с ними работают, собраны в классе,
# а часть данных скрыта от прямого доступа снаружи.
class BankAccount:

    def __init__(self, login, password, balance):
        # публичный атрибут — доступен отовсюду
        self.login = login
        # атрибуты с __ называются приватные:
        # Python прячет их имя как _BankAccount__password — напрямую не прочитать
        self.__password = password
        # атрибуты с _ называются защищенные:
        # это договорённость «не трогай снаружи», технически они доступны
        self._balance = balance

    # доступ к скрытым данным — только через метод с проверкой логина и пароля
    def get_balance(self, user_login, user_pass):
        if self.login == user_login and self.__password == user_pass:
            return self._balance
        return "Не верный логин или пароль !!"

    # приватный метод — внутренняя логика класса, снаружи напрямую не вызвать
    def __reset_pass(self):
        self.__password = "1234"
        return f"{self.login} Пароль сброшен новый пароль 1234!!"

    # публичный метод проверяет старый пароль и лишь потом меняет его
    def new_pass(self, old_pass):
        if old_pass == self.__password:
            return self.__reset_pass()
        return "Неверный старый пароль !!"

# ardager = BankAccount("ardager_dev", "2638", 780400583)
# print(ardager.get_balance("ardager_dev", "2638"))
# до приватного атрибута можно добраться через его «спрятанное» имя, но так делать не стоит
# print(ardager._BankAccount__password)
# print(ardager._BankAccount__reset_pass())
# print(ardager._BankAccount__password)
#
from abc import ABC, abstractmethod
#
# Абстрактный класс — «шаблон»: создать его объект нельзя (Animal() даст TypeError).
# @abstractmethod — метод без реализации: каждый наследник обязан определить его сам.
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def voce(self):
        pass

class Dog(Animal):
    def move(self):
        print('Steps')
    def voce(self):
        print("Gaf Gaf")
class Cat(Animal):
    def move(self):
        print('Step')
    def voce(self):
        print("May MAy")


gufi = Dog()
gufi.move()
gufi.voce()
print("===========")
cat = Cat()
cat.move()
cat.voce()
# print(gufi.move(), gufi.voce())
# print(gufi.move(), gufi.voce())
# создание кошки в try/except: если бы Cat не реализовала все абстрактные методы,
# объект создать было бы нельзя, и возникла бы ошибка TypeError
# try:
#     barsik = Cat()
#     barsik.move()
#     barsik.voce()
# except TypeError as e:
#     print(f"Ошибка: {e}")