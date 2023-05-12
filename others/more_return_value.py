# more than return value in python

def cal(num1, num2):
    add = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 // num2
    return add,minus,mul,div

n1,n2 = 100,50
a,b,c,d = cal(num2=n2, num1=n1)
print(f"{n1}+{n2}={a}")
print(f"{n1}-{n2}={b}")
print(f"{n1}*{n2}={c}")
print(f"{n1}//{n2}={d}")
