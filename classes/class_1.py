class Demo:
    def __init__(self, a):
        self.a = a
    def m(self):
        return self.a

obj1 = Demo(10)
print(obj1.m())
