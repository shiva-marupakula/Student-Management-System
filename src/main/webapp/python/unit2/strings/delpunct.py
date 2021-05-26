# to delete all punctuations from a string
s=input('enter any string')
s1=''
for i in s:
	if(i.isalpha()):
		s1=s1+i
print(s1)
