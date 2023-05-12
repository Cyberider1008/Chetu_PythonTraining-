def arm(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum +=digit ** 3
        temp //= 10
    return sum

num = int(input("enter your number: "))
result = arm(num)

if num == result:
    print("this is armstrong",result)
else:
    print("this is not armstrong")


