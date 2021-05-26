#to convert into binary code.
while(1):
	n=int(input('enter any number'))
	if(n==999):
		break
	elif(n>0):
		print('binary value is',bin(n))
	else:
		print("re-enter num")
