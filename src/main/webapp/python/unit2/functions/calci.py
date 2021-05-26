def add(a,b):
	s=a+b
	print(s)
def sub(a,b):
	d=a-b
	print(d)
def mul(a,b):
	m=a*b
	print(m)
def div(a,b):
	d1=a/b
	print(d1)
a=int(input('enter 1st value(a):'))
b=int(input('enter 2nd value(b):'))
c=input('enter operator(a=addition,s=substraction,m=multiplication,d=division):')
if(c=='a'):
	add(a,b)
elif(c=='s'):
	sub(a,b)
elif(c=='m'):
	mul(a,b)
if(c=='d'):
	div(a,b)
