# TO CHECK BIGGEST NUMBER AMONG THREE.
a=int(input('enter first num'))
b=int(input('enter second num'))
c=int(input('enter third num'))
if(a>=b and a>=c):
	print(a,'is biggest number')
if(b>=a and b>=c):
	print(b,'is biggest number')
else:
	print(c,'is biggest number')
