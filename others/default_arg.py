# default argument use in python

def cal(num1, num2, choice="+"):
    if choice == '+':
        return num1 + num2
    if choice == '*':
        return num1 * num2
    if choice == '-':
        return num1 - num2
    else:
        return "invalid"

mul = cal(100, 50, '*')
minus = cal(100, 50, '-')
default = cal(100,50)
default1 = cal(100,50,'/')
print(mul)
print(mul)
print(minus)
print(default)
print(default1)


