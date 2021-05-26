# a Python program to remove an item from a tuple
mytuple=(11,22,33,44,55,66,77,88,99,110,120)
mylist=list(mytuple)
mylist.remove(33)
remtuple=tuple(mylist)
print(remtuple,'is a tuple after removing an item')

