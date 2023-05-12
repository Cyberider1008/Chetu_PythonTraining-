def fact1(n):
    factorial = 1
    count = n
    while count > 0:
        factorial *= count
        count -= 1

    return factorial


while True:
    num = int(input("enter your value"))
    result = fact1(num)
    print("result is",result)
    print()
    stop1 = input("do want to continue this loop(yes/no): ")
    if stop1 == "no":
        break

