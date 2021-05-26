import random
a=random.randint(1,1000)
c=0
while(1):
	c=c+1
	if(c==10):
		break
	n=int(input('enter any number'))
	if(n==a):
		print('congratulations you wiil meet a great person soon')
		break
	elif(n>a):
		print('better luck next time aim low')
	else:
		print('better luck next time aim high')
