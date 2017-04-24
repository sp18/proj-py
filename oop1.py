#/usr/bin/python

#class Employee(object): # this is required form 
class Employee:	
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.'  + last + '@company.com'
		
		Employee.num_of_emps += 1 
		
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
	
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount
	
	# @ class methods as Alternative constructor	
	@classmethod
	def from_string(cls,emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	
	@staticmethod
	def is_workday(day):
		if(day.weekday() == 5 or day.weekday() == 6):
			return False
		return True

class Developers(Employee):
	def __init__(self,first,last,pay,prog):
		super().__init__(first,last,pay) # Python 3.x version
		#super(Developers,self).__init__(first,last,pay) # Python 2.x version
		self.prog = prog

class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print_emp(self):
		for emp in self.employees:
			print ('-->', emp.fullname())

		

dev_1 =Developers('Corey', 'Schafer', 50000,'python')
dev_2 = Developers('Test', 'User', 60000, 'java')

print(dev_1.prog)

mgr_1 = Manager('Sue','Forrest', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
'''
import datetime
my_date = datetime.date(2017, 4, 24)

print Employee.is_workday(my_date)
Employee.set_raise_amt(1.05)

print Employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount

print Employee.num_of_emps



emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)
print new_emp_1.email
'''

