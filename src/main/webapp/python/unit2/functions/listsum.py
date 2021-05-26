def listsum(mylist):
	if(len(mylist)==1):
		return mylist[0]
	else:
		return mylist[0]+listsum(mylist[1:])
mylist=[]
s=int(input('enter size of list:'))
for i in range(1,s+1):
	ele=int(input('enter elements:'))
	mylist.append(ele)
print(mylist)
print(listsum(mylist),'sum of list')
