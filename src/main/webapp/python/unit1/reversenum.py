#to print reverse number.
s=0
n=int(input('enter any number'))
while(n!=0):
	r=n%10
	s=(s*10)+r
	n=n//10
print(s,"is reverse number")
