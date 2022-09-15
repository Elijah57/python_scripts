"""
1. create a python class Person with attributes: name and age of type string
2. create  a display() method that displays the name and age of an object created via the Person class
3. create a child class student which inherits from the Person class and which also havea section attribute
4. create a method displayStudent() that display the name, age and section of an object created with the 
student class
5. create a student objec via an instantiation of the student class and then test the displayStudent() method
"""

class Person:

	def __init__(self, name: str, age: str):
		"""Initializing the attributes
		Args:
			name: str the name of the object
			age: str, the age of the object

		Returns:
			None
		"""
		self.name = name
		self.age = age

	def __repr__(self):
		return f"Person({str(self.name)}, {str(self.age)})"

	def display(self):
		"""Displays the attributes of the object(Person)"""
		print("==========")	
		print(f"Name : {self.name}")
		print(f"Age : {self.age}")
		print("==========\n")




class Student(Person):

	def __init__(self, name: str, age: str, section: str):
		"""Initializing the attributes
		Args:
			name: str the name of the object
			age: str, the age of the object
			section: str, the section of the student

		Returns:
			None
		"""		
		Person.__init__(self, name, age)
		self.section = section

	def __repr__(self):
		return f"Student({str(self.name)}, {str(self.age)}, {str(self.section)})"

	def displayStudent(self):

		"""Displays the attributes of the object(Person)"""
		print("==========")	
		print(f"Name : {self.name}")
		print(f"Age : {self.age}")
		print(f"section : {self.section}")
		print("==========\n")





obi = Person("Obi", "39")
obi.display()
print(obi)

student1 = Student("Chioma", "40", "5C")
student1.displayStudent()
print(student1)
