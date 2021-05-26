import op
a=int(input('enter 1st value(a):'))
b=int(input('enter 2nd value(b):'))
c=input('enter operator(a=addition,s=substraction,m=multiplication,d=division):')
if(c=='a'):
	op.add(a,b)
elif(c=='s'):
	op.sub(a,b)
elif(c=='m'):
	op.mul(a,b)
if(c=='d'):
	op.div(a,b)
