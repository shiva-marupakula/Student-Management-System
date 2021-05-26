mylist=[1,23,34,5,66,7,8,9,0,'shiva','hi','hello']
#Print the elements
print(mylist)
#Print the size of the list
l=len(mylist)
print(l,'is length of list')
#Print first and last element
print(mylist[0],'is first element')
print(mylist[-1],'is last element of list')
#print duplicate elements in a list
duplicate=[]
for i in mylist:
	if i not in duplicate:
		if(mylist.count(i)>1):
			duplicate.append(i)
print(duplicate,'is list of duplicate elements')
#Print last 3 elements
print(mylist[-3:],'are last three elements')
#print entire list except last 3
print(mylist[0:-3],'are element of list except last 3')
# to Update any index value with an user given element
e=int(input('enter any element'))
index=int(input('enter index  number'))
mylist[index]=e
print(mylist)
#to Update 2 to 5 indexes with 100
mylist[2:6]=[100,100,100,100]
print(mylist)
#to print the updated list and new length of the list
print(mylist,'is updated list')
print(len(mylist),'is length of list')
#to Remove any element given by user
r=int(input('enter any number that you Want to remove:'))
mylist.remove(r) 
print(mylist,'is list after removing',r,'value')
#to delete elements from 3 to 6 locations
del mylist[3:6]
print(mylist,'is after deleting elements')
#to print the index of a element given by user
ele=int(input('enter any element which present in list'))
print(mylist.index(ele),'is index of element given by user')
#to check the list size if the size of the list is less than 10 then add remaining elements

if(len(mylist)<10):
	item=int(input('enter a value that you want to append to a list'))
	mylist.append(item)
print(mylist)


