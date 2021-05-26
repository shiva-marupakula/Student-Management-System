# To calculate bonus of employee
salary=int(input('enter your salary'))
if(salary<10000):
	ts=salary+(salary*0.02)
else:
	ts=salary
g=input('enter gender(M or F) ')
name=input('enter your name')
if(g!='F'):
	bonus=ts*0.05
	tswb=ts+bonus
	print('{}your bonus amt is{}then your total salary with your bonus{}'.format(name,bonus,tswb))
else:
	bonus=ts*0.1
	tswb=(bonus+ts)
	print('{} your bonus amt is {} then your total salary with bonus{}'.format(name,bonus,tswb))
