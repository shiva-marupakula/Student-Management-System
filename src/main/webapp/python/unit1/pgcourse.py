# to check eligibility for pg courses
name=input('enter your name')
s=float(input('enter your ssc percentage'))
i=float(input('enter inter percentage'))
exm=float(input('enter pg exam percentege'))
strm=input(' do you want to change stream y or n')
if(s>=80 and i>=80):
	if(strm=='y'or strm=='Y'):
		fexm=(exm-5)
		if(fexm>70):
			print( name,'you are eligible for PG course')
		else:
			print(name,'you are not eligible for PG course')
	else:
		if(exm>70):
			print( name,'you are eligible for PG course')
		else:
			print(name,'you are not eligible for PG course')
else:
	print(name,'you are not eligible for PG course')
