try:
	a=int(input('enter any number'))
	b=int(input('enter any number'))
	d=a/b
except ZeroDivisionError:
	print('enter other than zero')
else:
	print(d)
finally:
	print('thank you')

