class Employee:
    #def __init__(self,name,age):
     #   self.name = name
      #  self.age = age
    def emp1(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return self.name, self.age

cl1 = Employee()

cl1.emp1('ashish1',46)
n,a =cl1.display()
print(n,a)

