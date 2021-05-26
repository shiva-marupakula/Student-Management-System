# to check whether given number is armstrong or not.
n=int(input('enter any number'))
l=len(str(n))
temp=n
a=0
while(n!=0):
	r=n%10
	a=a+(r**l)
	n=n//10
if(temp==a):
	print(a,'is armstrong')
else:
	print(a,'is not armstrong')
