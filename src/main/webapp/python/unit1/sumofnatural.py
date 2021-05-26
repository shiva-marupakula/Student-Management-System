#to print sum of n natural numbers
n=int(input('enter any number'))
s=0
for i in range(1,n+1):
	s=s+i
print(s,"is sum of" + n +"natural numbers")
