set1={}
print(type(set1))
set2=set()
print(type(set2))
set2.add('shiva')
print(set2)
set2.update([1,2,3,4,5,6,7,11,22,33,44,55,66])
print(set2)
set2.discard(22)
set2.discard(99)
print(set2)
set2.pop()
print(set2)
set2.remove(11)
print(set2)
set2.clear()
print(set2)
#union of two sets
a={1,2,3,4,5,6,7}
b={11,22,33,44,55,6667,1,2,3}
print(a|b)
print(a.union(b))
print(b.union(a))
#intersection of sets
print(a&b)
print(a.intersection(b))
print(b.intersection(a))
#difference of two sets
print(a,'a')
print(b,'b')
print(a-b,'a-b')
print(b-a,'b-a')
print(a.difference(b),'a.difference(b)')
print(b.difference(a),'b.difference(a)')
# symmetric_difference
print(a^b,'a^b')
print(b^a,'b^a')
print(a.symmetric_difference(b),'a.symmetric(b)')
print(b.symmetric_difference(a),'b.symmetric(a)')
s={11,22,33,44,55,66,77,88,99}
print(s)
#built in functions
print(all(s),'using all function')
print(any(s),'using any fuction')
print(max(s),'using max functon')
print(min(s),'using min function')
print(len(s),'using len fuction ')
print(sorted(s),'using sorted function')
print(enumerate(s),'using enumerate function')
print(sum(s),'sum function')
# creating set by using for loop
myset=set()
n1=int(input('enter size of your set:'))
for i in range(1,n1+1):
	ele=int(input('enter any item '))
	myset.add(ele)
print('myset:',myset)
