mydict={12:'a',34:'shiva',66:'rgukt'}
mydict.popitem()
print(mydict)
del mydict[12]
print(mydict)
mydict.clear()
print(mydict)
#to crear dictionary using user input
dict1={}
n=int(input('enter no. of pairs'))
for i in range(1,n+1):
	key=int(input('enter key value'))
	val=int(input('enter value that you want to insert yo dictionary'))
	dict1[key]=val
print(dict1)
print(dict1.values())
print(dict1.items())
print(len(dict1),'lenght')
