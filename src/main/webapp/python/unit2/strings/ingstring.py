#to add 'ing' at the end of string if string already endswith ing add ly if length is lessthan 3 leave it unchange
string1=input('enter any string')
if(len(string1)<3):
	print(string1)
else:
	if(string1.endswith('ing')):
		string1=string1+'ly'
		print(string1)
	else:
		string1=string1+'ing'
		print(string1)
