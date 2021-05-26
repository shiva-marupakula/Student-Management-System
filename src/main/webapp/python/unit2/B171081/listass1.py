#to find the sum of all numbers in a list
mylist=[1,2,3,4,5,6]
i=0
s=0
while(i<len(mylist)):
	ele=mylist[i]
	s=s+ele
	i=i+1
print('sum of numbers of list is',s)
