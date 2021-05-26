# to print frequency of letter which are present in a string
s=input('enter any string')
mylist=s.split()
new=[]
mydict={}
for i in mylist:
	if(i not in new):
		new.append(i)
		c=mylist.count(i)
		mydict[i]=c
print(mydict)
