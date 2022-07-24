class Wife:
    def __init__(self,name, age, weight):
        self.name = name
        self.set_age(age)
        self.__weight = weight

    age = property()

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 21 <= value <=31:
            self.__age = value
        else:
            raise ValueError


w01 = Wife("MI", 30, 70)
print(w01)