class Employee:
	def __init__(self,first,last,sal):
		self.f=first
		self.l=last
		self.s=sal
	def fullname(self):
		return "full name  is:{} {}".format(self.f,self.l)

emp1=Employee('shiva','marupakula',10000)
emp2=Employee('shivaji','chatrapathi',120000)
print(emp1.fullname())
print(emp2.fullname())
