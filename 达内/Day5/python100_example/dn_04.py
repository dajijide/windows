class Vetory:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "結果是"+str(self.x)

    def __sub__(self, other):
        return Vetory(self.x - other)


v01 = Vetory(10)
print(v01 - 2)
