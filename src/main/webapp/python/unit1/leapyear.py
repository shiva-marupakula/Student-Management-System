#to check whether year is leap year or not.
year=int(input('enter the year '))
if((year%4==0 and year%100!=0)or(year%400==0)):
	print(year,'year is leap')
else:
	print(year,'year is not a leap')
