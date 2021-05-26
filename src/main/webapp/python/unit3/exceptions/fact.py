import math
mylist=[1,2,3,4,-4,'shiva',12]
for i in mylist:
	try:
		print(math.factorial(i))
	except ValueError:
		print(i,'enter positive numbers only ')
	except TypeError:
		print('enter integers only',i)
	
