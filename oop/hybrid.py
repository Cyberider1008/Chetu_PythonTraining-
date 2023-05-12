# hybrid inheritance

class Bsp:
    def f1(self):
        print("this is my party")

class Kamlesh(Bsp):
    def f2(self):
        print(" I am kamlesh")

class Mayawati(Bsp):
    def f3(self):
        print("i am mayawati")

class Child(Kamlesh, Mayawati):
    def f3(self):
        print(" I am child")


c = Child()
c.f1()
