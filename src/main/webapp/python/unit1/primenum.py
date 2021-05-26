# to check whether given number is prime or not
n=int(input('enter any num'))
if(n>1):
	for i in range(2,n):
		if(n%i==0):
			print('it is not prime')
			break
	else:
		print('it is prime number')
else:
	print('it is not prime number')
