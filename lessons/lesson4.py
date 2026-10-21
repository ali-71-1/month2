# Атрибуты класса общие для всех объектов, атрибуты объекта — у каждого свои.
class User:
    class_names = ['M', 'F']  # атрибут класса
    count = 0                 # общий счётчик созданных объектов

    def __init__(self, first_name, last_name):
        # атрибуты объекта
        self.first_name = first_name
        self.last_name = last_name
        # при создании каждого объекта увеличиваем общий счётчик
        User.count += 1

    # @property — метод вызывается как атрибут, без скобок: maksat.full_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @staticmethod — метод без self, не зависит ни от объекта, ни от класса
    @staticmethodpy
    def add(a, b):
        return a + b

    # @classmethod — получает не объект (self), а сам класс (cls)
    @classmethod
    def get_user_count(cls):
        return cls.count

maksat = User("Max", "Smith")
print(maksat.full_name)
print(User.get_user_count())
print(User.count)
# меняем атрибут класса — изменение общее для всех объектов
User.class_names += ['X']