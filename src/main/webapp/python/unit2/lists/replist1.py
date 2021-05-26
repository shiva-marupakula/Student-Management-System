# replacing values of list
mylist=[1,2,3,4,5,'shiva','hi',9]
mylist[2]='msg'
mylist[0:2]=['ss',99,88]
mylist.append('t')
print(mylist)
mylist.insert(2,'ias')
print(mylist)
mylist.extend([9,8,7,6,'kk'])
print(mylist)
mylist[4:4]=[12,13,14,15,16]
print(mylist)
mylist[2:5]=['hg']
print(mylist)
mylist[2:4]=[1,2,3,4,5,6,7,8,9]
print(mylist)
del mylist[0]
print(mylist)
mylist.clear()
print(mylist)
