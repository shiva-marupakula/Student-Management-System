n=int(input('enter lenght of list:'))
list1=[]
for i in range(0,n):
	ele=int(input('enter any element:'))
	if(ele>=100):
		list1.append('excess')
	else:
		list1.append(ele)
print(list1)
