import sys
class Demo:
    pass

d1 = Demo()
d2 = d1
d3 = d2
d4 =d1

print("it's total(d1,d2,d3,d4) objectcount with self ",sys.getrefcount(d1))
