# 生成器原理
"""
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self,stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self
    def __next__(self):
        if self.begin >= self.stop_value
            raise StopIteration
        temp = self.begin
        self.begin += 1
        return temp
"""


def my_range(stop_value):
    number = 0
    while number < stop_value:
        yield  number

my_01 = my_range(10)
print(type(my_01),dir(my_01))
print(id(my_01).__init__(),id(my_01))

for item in my_01:
    print(item)