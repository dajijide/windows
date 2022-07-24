class Wife:
    count = 0
    def __init__(self,name):
        self.name = name
        Wife.count += 1
    @classmethod
    def class_print(cls):
        print("我有%d房" % cls.count)



wf01 = Wife("xioaemi")
wf02 = Wife("jsdh")
Wife.class_print()


class Enemy:
    def __init__(self,name, blood, basic_attack, defend):
        self.name = name
        self.blood = blood
        self.basic_attack =basic_attack
        self.defend = defend
    def print_info(self):
        print(self.name, self.blood, self.basic_attack, self.defend)


list = [
    Enemy("meiba", 100, 20, 20)
]