mylist=[1,2,3,4,5,6,7,8,9,'shiva','ss']
mylist[1]='shiva sai'
print('my list after inserting one element is',mylist)
mylist[0:4:]=[11,22,33,44]
print('after inserting multiple elements [11,22,33,44] is:',mylist)
mylist.append('marupakula')
print('my list after appending element marupakula is:',mylist)
mylist.extend([99,88,77,666,555,12])
print(' mylist after updating by using extend method is:',mylist)
mylist.insert(0,'msg')
print('mylist after inserting element is:',mylist)
del mylist[0]
print('mylist after deleting one element:',mylist)

