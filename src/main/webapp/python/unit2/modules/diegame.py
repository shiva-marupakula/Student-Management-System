import random
r=True
while(r):
	a=random.randint(1,6)
	print(a)
	print('are you want to continue Y or N')
	r='Y' in ((input('enter choice')))

