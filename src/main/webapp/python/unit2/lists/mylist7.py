mylist=[2,7,2,4,8,7,7]
n=int(input('enter any num'))
for i in range(0,len(mylist)):
	if(mylist[i]==n):
		print('index of {} is {}'.format(n,i))
print('count is',mylist.count(n))
