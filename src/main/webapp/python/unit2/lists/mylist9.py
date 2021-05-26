n=input('enter any string')
new=[]
for i in n:
	if(i not in ['a','e','i','o','u','A','E','I','O','U']):
		new.append(i)
print(new)
