# to check maximum among three
a=int(input('enter 1st num'))
b=int(input('enter 2nd num'))
c=int(input('enter 3rd num'))
if(a>b and a>c):
	print(a,'is largest num among three')
elif(b>a and b>c):
	print(b,'is largest num among three')
else:
	print(c,'is largest num among three')
