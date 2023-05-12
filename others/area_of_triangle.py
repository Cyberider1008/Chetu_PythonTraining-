#calculate the area of a triangle

a = float( input( "enter the first sides:"))
b = float( input( "enter the second  sides:"))
c = float( input( "enter the Third  sides:"))

s = ( a + b + c ) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("the area of triangle is %0.2f" %area)
