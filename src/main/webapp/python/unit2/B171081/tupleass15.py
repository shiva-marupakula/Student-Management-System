#Python program to count the elements in a list until an element is a tuple.
mytuple=(11,12,23,34,(1,2,3,45),4)
c=0
for i in mytuple:
	if(type(i)==tuple):
		print('sum is ',sum(i))
		break
	else:
		c=c+1
print('count is',c)
