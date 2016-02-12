class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'

x = MyClass();
print(x.i)
print(x.f())
print(x.__doc__)
print(x.data)
print(MyClass.f(x))