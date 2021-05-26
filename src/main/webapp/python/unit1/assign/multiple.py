#to check whether first num is  multiple of other one
a=int(input('enter first num'))
b=int(input('enter secondnum'))
if(b%a==0):
	print('{} is multiple of {}'.format(a,b))
else:
	print('{} is not multiple of {}'.format(a,b)) 
