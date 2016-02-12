def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

c = C()
print(c.f(1,2))
print(c.g())
print(c.h())

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

b = Bag()
print(b.data)
b.add(21)
print(b.data)
b.addtwice(33)
print(b.data)