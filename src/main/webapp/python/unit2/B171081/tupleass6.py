#a Python program to find the repeated items of a tuple
mytuple=(1,2,3,4,5,6,7,8,9,0,11,111,111,1111,1111)
new_tuple=[]
for i in mytuple:
	if i not in new_tuple:
		if(mytuple.count(i)>1):
			new_tuple.append(i)
duplicate_tuple=tuple(new_tuple)
print("repeated items are",duplicate_tuple)
