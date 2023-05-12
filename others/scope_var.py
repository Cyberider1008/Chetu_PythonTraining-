# scope variable

def f1():
    a = 10
    print(id(a))

a = 10
f1()
print(id(a))
