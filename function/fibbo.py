def fib(n):
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1

fib(8)

