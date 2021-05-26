# to remove duplicate elements from a list
mylist=[1,2,3,4,3,2,4,5,6,7,8]
new=[]
for i in mylist:
	if i not in new:
		new.append(i)
print(new)
