# to check whether given num is perfect number or not
def per(n):
	s=0
	for i in range(1,n):
		if(n%i==0):
			s+=i
	if(n==s):
		print('given number is perfect number')
	else:
		print('given number is not a perfect number')
p=int(input('enter any number:'))
per(p)
	
