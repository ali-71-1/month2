# Множественное наследование
class Flying:
  #
    def fly(self):
        print("лечу")

class Swimming:
#
    def swim(self):
        print("плыву")

class Duck(Flying, Swimming):
    pass

donald = Duck()



