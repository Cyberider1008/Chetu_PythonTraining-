# single inheritance

class Parent:
    def m1(self):
        print("Home")


class Child(Parent):
    pass

c = Child()
c.m1()

