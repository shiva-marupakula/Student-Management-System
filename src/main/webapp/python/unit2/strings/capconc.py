# to  concatenate all capital latters in string
s1=input('enter first string')
s2=input('enter second string')
s=s1+s2
new=''
for i in s:
	if(i.isupper()):
		new=new+i
print(new)
