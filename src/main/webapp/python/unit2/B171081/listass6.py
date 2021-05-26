#a program that creates a list of numbers from 1-50 that is either divisible by 3 or divisible by
divisible=[]
for i in range(1,50):
	if(i%3==0 or i%6==0):
		divisible.append(i)
print(' list of numbers which are divible by 3 or by 6',divisible)
