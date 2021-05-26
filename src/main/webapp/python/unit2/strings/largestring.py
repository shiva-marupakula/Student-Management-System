mylist=['shiva','rguktbas','marupakula','kalamma','balaiah','allpowerswithinyou']
list1=[]
for i in mylist:
	l1=len(i)
	list1.append(l1)
ml=max(list1)
for j in mylist:
	if len(j)==ml:
		print(j)
