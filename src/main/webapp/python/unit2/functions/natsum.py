def natsum(n):
	if(n==1):
		return(1)
	else:
		return(n+natsum(n-1)
n=int(input('enter any num'))
print(natsum(n))
