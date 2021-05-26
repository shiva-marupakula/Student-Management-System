#to convert lower case to upper case and upper case to lower case.
n=input('enter any character')
if(n.isupper()):
	L=n.lower()
	print(L,'is lower case')
elif(n.islower()):
	U=n.upper()
	print(U,'is upper case')
else:

	print(n,'is neither lower or upper case')
