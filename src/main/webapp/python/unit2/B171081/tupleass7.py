#a Python program to check whether an element exists within a tuple.
mytuple=('shiva','marupakula','B171081','puc-2','rguktbasar')
n=input('enter a string to check whether an element exists within  tuple:')
for i in mytuple:
	if(i==n):
		print(n,'is exist in tuple')
		break
else:
	print(n,'is not exist in tuple')
	
