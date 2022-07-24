class AttackError(Exception):
    def __init__(self, message, error_line, age_value):
        super().__init__("出错了")
        self.message = message
        self.error_line = error_line
        self.age_value = age_value

class Enemy:
    def __init__(self,age):
         self.attack = age

    @property
    def attack(self):
         return self.__age

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 100:
             self.__age = value
        else:
            raise AttackError("超出范围了", value, 26, 10086)

try:
    ACK = Enemy(200)
except AttackError as a:
    print(a.message)
    print("请重新输入")