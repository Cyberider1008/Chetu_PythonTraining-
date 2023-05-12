def cal(num1, num2, choice):
    def sum(first, second):
        return first + second
    if choice == '+':
        return sum(num1, num2)
    else:
        return 'invalid'

res = cal(100, 50, '+')
print(res)
