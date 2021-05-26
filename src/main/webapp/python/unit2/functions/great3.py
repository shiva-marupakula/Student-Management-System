# to check greatest num among three
def great(x,y,z):
	if(x>=y and x>=z):
		print(x,'is greater')
	elif(y>=z and y>=x):
		print(y,'is greater')
	else:
		print(z,'is greater')
a=int(input('enter 1st value:'))
b=int(input('enter 2nd valuue:'))
c=int(input('enter 3rd value:'))
great(a,b,c)
