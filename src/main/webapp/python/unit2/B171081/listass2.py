# to find sum of all even numbers present list
mylist=[11,22,33,44,55,66,77,88,99,110]
print(mylist)
s=0
for i in mylist:
	if(i%2==0):
		s=s+i
print('sum of even numbers is',s)
