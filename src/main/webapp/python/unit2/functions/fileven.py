# program using filter function 
mylist=[1,2,3,4,5,6,7,8,9]
s=filter(lambda x:(x%2==0),mylist)
print(list(s))
