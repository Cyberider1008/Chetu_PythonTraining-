class Person:
    '''this is class method and static method '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def frombirth(cls, name1, year):
        return cls(name1, 2021 - year)

    @staticmethod
    def confirm_age(age):
        return (age > 18)


p1 = Person('ashish', 34)
p2 = Person.frombirth('mayan', 2001)

print(p1.age)
print(p2.age)

print(p1.name)

print(p2.name)


print(Person.confirm_age(34))
