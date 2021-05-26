#program to get s string made of the first 2 and the last 2 characters from a givensrting.if the string length is less than 2, return the original stirng instead of empty string
s=input('enter any string')
if(len(s)<2):
	print(s)
elif(len(s)<4):
	print(s[0]+s[-1])
else:
	print(s[:2]+s[-2:])
