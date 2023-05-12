# calculator program

# add two number

def add(x,y):
    return x+y

# subtract  two number

def sub(x,y):
    return x-y

# multiplication  two number

def mul(x,y):
    return x*y

# division  two number

def div(x,y):
    return x/y

print("select operation")
print("1.add")
print("2.min")
print("3.mul")
print("4.div")


while True:
    choice=input("enter choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        num1=float(input("enter first no.: "))
        num2=float(input("enter second  no.: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "+", num2, "=", sub(num1, num2))
        elif choice == '3':
            print(num1, "+", num2, "=", mul(num1, num2))
        elif choice == '4':
            print(num1, "+", num2, "=", div(num1, num2))
        nxt_cal = input("next calaculation? (yes/no): ")
        if nxt_cal == "no":
            break
    else:
        print("invalid input")

    






