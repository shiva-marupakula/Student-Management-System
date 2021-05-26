#to print factorial of given number  
n=int(input('enter any number'))
fact=1
if(n<0):
	print('please enter positive values  only')
elif(n==0):
	print('factorial of 0 is 1')
else:
	for i in range(1,n+1):
		fact=fact*i
	print('factorial of {} is {}'.format(n,fact))
