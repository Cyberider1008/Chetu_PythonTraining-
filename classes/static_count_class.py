class Employee:
    count = 0
    def __init__(self, id, name, lname, age, salary):
        self.id = id
        self.name = name
        self.lname = lname
        self.age = age
        self.salary = salary
        Employee.count += 1
    
    def display(self):
        return self.id, self.name, self.lname, self.age, self.salary

emp1 = Employee(3,'ashish','kumar',56,780000)
emp2 = Employee(3,'ashish','kumar',56,780000)
emp3 = Employee(3,'ashish','kumar',56,780000)
i, n, l, a, s=emp1.display()
print(i,n,l,a,s)
print(Employee.count)









