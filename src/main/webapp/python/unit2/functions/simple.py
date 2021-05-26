# to calculte simple calculate
def simple(p,t,s):
	if(s=='y'):
		print((p*t*12)/100),'is simple interest for senior citizens')
	else:
		print((p*t*13)/100),'is simple interest for other than s.citizens')
p=float(input('enter the principal amount'))
t=float(input('enter the duration '))
s=input('is customer is senior citizen y/n')
simple(p,t,s)
