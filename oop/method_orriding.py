# method orriding

class Parent:
    def property(self):
        print("Gols|cash|Land")
    def marry(self):
        print("Mayawati...")

class Kunal(Parent):
    def marry(self):
        print("Madhri...")

k = Kunal()
k.property()
k.marry()

