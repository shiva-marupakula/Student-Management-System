# to calculate area of triangle using heron's formula.
a=int(input('enter length of the first side'))
b=int(input('enter lenght of sec side'))
c=int(input('enter length of third side'))
s=((a+b+c)/2)
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print ("area of triangle is",area)

