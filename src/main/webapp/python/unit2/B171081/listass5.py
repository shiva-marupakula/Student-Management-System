#a program that counts the number of times a value appears in the list
mylist=[1,2,3,65,11,1,33,11,1,2,3,4]
n=int(input('enter any value'))
c=0
for i in mylist:
	if(i==n):
		c=c+1
print('frequenccy is ',c)

