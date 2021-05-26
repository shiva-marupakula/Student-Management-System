# to print sum of nested tuple
mytuple=(1,2,3,4,(11,12,13,14),'shiva')
c=0
for i in mytuple:
	if(type(i)==tuple):
		print('sum is ',sum(i))
		break
	else:
		c=c+1
print("count is",c)
