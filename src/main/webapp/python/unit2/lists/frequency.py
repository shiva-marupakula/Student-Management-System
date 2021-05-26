mylist=[2,3,4,4,4,4,5,6,7,77,7,2,2,2,0]
m=[]
a=[]
for i in mylist:
	if i not in m:
		m.append(i)
		c=mylist.count(i)
		a.append('{}:{}'.format(i,c))
print(a)
