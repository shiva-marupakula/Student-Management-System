#Write a Python program to replace last value of tuples in a list. 
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
my_list=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new=[]
for i in my_list:
	new.append(i[:-1]+(100,))
print(new)
