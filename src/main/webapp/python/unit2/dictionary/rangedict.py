#to create dictionary 
mydict={}
for i in range(1,16):
	mydict[i]=i**2
print(mydict)
print(max(mydict),'maximum key value')
print(min(mydict),'is minimum keyvalue in dictionary')
print(max(mydict.values()),'is max value')
print(min(mydict.values()),'is min of values')
