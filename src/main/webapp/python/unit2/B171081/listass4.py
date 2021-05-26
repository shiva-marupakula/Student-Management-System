#to find whether a particular element is present in the list using a loop
mylist=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55]
n=int(input('enter any number you want'))
for i in mylist:
	if(i==n):
		print('number is present in list')
		break
else:		
	print('nnumber is not present in list')

