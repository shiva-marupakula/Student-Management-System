# To check  type input
n=input('enter any character')
if(n.isalpha()):
	print('you entered alphabet')
elif(n.isdigit()):
	print('you entered digit')
else:
	print('you entered special character') 
