# to check whether eleme,t is exist in tuple or not
mytuple=(1,2,2,3,34,4,5,6)
n=int(input('enter any element'))
for i in mytuple:
	if(i==n):
		print('element found')
		break
else:
	print('element not found') 
