# to remove nth index of string
s=input('enter a string')
n=int(input('enter index number '))
if(len(s)==0):
	print('empty string')
else:
	s1=s[:n]
	s2=s[n+1:]
	print((s1+s2),'after removing particular index value')
