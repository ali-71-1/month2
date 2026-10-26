# # # # | Метод         | Что делает                |
# # # # | ------------- | ------------------------- |
# # # # | `__init__`    | конструктор               |
# # # # | `__str__`     | вывод через `print()`     |
# # # # | `__repr__`    | отображение объекта       |
# # # # | `__len__`     | `len(obj)`                |
# # # # | `__getitem__` | `obj[key]`                |
# # # # | `__call__`    | вызов объекта как функции |
# # # # | `__eq__`      | `==`                      |
# # # # | `__lt__`      | `<`                       |
# # # # | `__gt__`      | `>`                       |
# # #
# # #
# # # # | Оператор | Магический метод | Пример   |
# # # # | -------- | ---------------- | -------- |
# # # # | `+`      | `__add__`        | `a + b`  |
# # # # | `-`      | `__sub__`        | `a - b`  |
# # # # | `*`      | `__mul__`        | `a * b`  |
# # # # | `/`      | `__truediv__`    | `a / b`  |
# # # # | `//`     | `__floordiv__`   | `a // b` |
# # # # | `%`      | `__mod__`        | `a % b`  |
# # #
# class Test:
#
#     def __init__(self, value):
#         self.value = value
#     # print()
#     def __str__(self):
#         return self.value
# test_obj = Test("498530")
# my_int = 123
#
# print(my_int)
# print(test_obj)

    # def __call__(self, *args, **kwargs):
    #     print("Меня вызвали!!")

    # def __add__(self, other):
    #     return self.value + other.value
    # def __sub__(self, other):
    #     return self.value - other.value
    # def __mul__(self, other):
    #     return self.value * other.value
    # def __truediv__(self, other):
    #     return self.value / other.value
    # def __floordiv__(self, other):
    #     return self.value // other.value
    # def __mod__(self, other):
    #     return self.value % other.value


# obj_1 = Test(333)
# obj_2 = Test(2)
# my_inta_1 = 123
# my_inta_2 = 123

# data = obj_1 % obj_2
# print(data)

    # def __getitem__(self, item):
    #     # print(self.value)
    #     # print(item)
    #     return self.value[item]
# # #
# obj_1 = Test([1,2,4,5,6,7,9])
# print(obj_1)
# # # # my_int_2 = [1,4,5,6,7]
# # # # obj_1()
# # # # my_int_2()
# # # # print(data)
# # # # # print(type(test_obj))
# # # # # print(type(my_int))
# # # # print(my_int)
# # # # print(test_obj)
#
# class Video:
#
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#         self.view_count = 0
#
#
#     def __call__(self, *args, **kwargs):
#         self.view_count += 1
#         # print(f"Количество просмотров {self.view_count}")


# obj_1 = Video("Wind", "Наруто опенинг")
# obj_2 = Video("Bakr>", "New song")
# obj_3 = Video("Wind", "Наруто опенинг")
#
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# obj_1()
# print(f"количество просмотров {obj_1.view_count}")
# # #
# # #
# # class Math:
# # #     # Атрибуты  класса
# # #     name_class = "My math!!"
# # #
# #     def __init__(self, first_name, last_name):
# #         # Атрибуты объекта|экземпляра класса
# #         self.first_name = first_name
# #         self.last_name = last_name
# # #     def get_test(self):
# # #         pass
# # #     @staticmethod
# # #     def add_two_num(a, b):
# # #         return a + b
# # #     @classmethod
# # #     def get_name_class(cls):
# # #         return cls.name_class
# # #
# # #     @property
# # #     def full_name(self):
# # #         return f'{self.last_name} {self.first_name}'
# # #
# # #     @full_name.setter
# # #     def full_name(self, value):
# # #         print(value)
# # #
# # # ardager = Math("Ardager", "Kartanbekov")
# # #
# # # # print(ardager.first_name)
# # # print(ardager.last_name)
# # # ardager.last_name = "dfghjkl;"
# # # print(ardager.last_name)
# # # print(ardager.full_name)
# # # ardager.full_name = "dfghjkl; dfghjk"
# # # # print(ardager.full_name)
# # from abc import ABC, abstractmethod
# #
# #
# # class OTPSender(ABC):
# #     @abstractmethod
# #     def sent_otp_phone(self, phone):
# #         pass
# #
# # class Kg(OTPSender):
# #     def sent_otp_phone(self, phone):
# #         data = f'''
# #             <phone>{phone}</phone>
# #             <text>Ваш код 1234</text>
# #         '''
# #         return data
# #
# # class Ru(OTPSender):
# #     def sent_otp_phone(self, phone):
# #         data = {
# #             "Phone": phone,
# #             "txt": "Ваш код 1234"
# #         }
# #         return data
# #
# # # test = Kg()
#
# class Money:
#
#     def __init__(self, value, currency):
#         self.value = value
#         self.currency = currency
#
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return self.value + other.value
#         else:
#             raise ValueError("Ощибка!!")
#
#     def test(self):
#         pass
#
#
#
# som = Money(100, "SOM")
# usd = Money(100, "USD")
#
# som.test()
# my_balbance = som + usd

class Math:
    name_class = "My math"
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @staticmethod
    def add_two_num(a, b):
        return a + b
    @classmethod
    def get_name_class(cls):
        return cls.name_class
    @property
    def full_name(self):
        return f"{self.last_name} {self.last_name}"
    @full_name.setter
    def full_name(self, value):
        print(value)


ardager = Math("ali", "aliev")
# print(ardager.first_name)
# ardager.first_name = "alishka"
# print(ardager.first_name)
# print(ardager.last_name)
# ardager.last_name = "Alishka"
# print(ardager.last_name)
print(ardager.full_name)
ardager.full_name = "Muhammad  Mamiev"
print(ardager.full_name)
# print(ardager.full_name)
# #
# print(Math.add_two_num(15, 12))
# print(Math.get_name_class())
# obj_1 = Math(1, 2)
# print(obj_1.add_two_num(12, 2))
