n=int(input('enter number'))
c=0
s=0
while(n!=0):
	c=c+1
	s=s+(n%10)
	n=n//10
print('sum of digits',s)
print('number of digits',c)
