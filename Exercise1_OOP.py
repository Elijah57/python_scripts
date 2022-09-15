"""
1. write a rectangle class in python  allowing you to build a rectangle with length and width attribute
2. create a perimeter method to calculate the perimeter of the rectangle and an area method to calculate
the area of the rectangle
3. create a method display() that display the length, width, perimeter and area of the object using an 
instantiation on the rectangle class
4. create a parallelepipede child class inheriting from the rectangle class and with a height attribute
and another volume() method to calculate the volume of the parallelepipede
"""
#1
class Rectangle:

	def __init__(self, width: float, length: float):
		"""Initialising the class
		Args:
			width: float, the width of the rectangle
			length: float(or int) the length of the rectangle

		"""
		self.l = length
		self.w = width

	def perimeter(self):
		"""calculate the perimeter of the rectangle
		Args:
			None

		Returns:
			float, the perimeter of the rectangle
		"""
		return 2 * (self.l + self.w)

	def area(self):
		"""calculate the area of the rectangle
		Args:
			self

		Returns:
			float, the area of the rectangle
		"""
		return self.w * self.l 

	def __repr__(self):
		return f"Rectangle({self.w}, {self.l})"

	def display(self):
		"""Displays the attributes of the rectangle
		Args: 
			None

		Returns:
			None
		"""
		print("=========================")
		print(f"Length : {float(self.l)}")
		print(f"Width : {float(self.w)}")
		print(f"Perimeter : {float(self.perimeter())}")
		print(f"Area : {float(self.area())}")
		print("=========================\n")


class parallelepipede(Rectangle):

	def __init__(self, width, length, height):
		"""Initialising the class
		Args:
			width: float, the width of the object
			length: float(or int) the length of the object
			height: float (or int) the height of  the object

		"""		
		Rectangle.__init__(self, width, length)
		self.h = height

	def volume(self):
		"""calculate the volume of the parallelepipede
		Args:
			None

		Returns:
			float, volume of the object

		"""

		return self.h * self.w  * self.l	

	def display(self):
		"""Displays the attributes of the rectangle
		Args: 
			None

		Returns:
			None
		"""
		print("=========================")
		print(f"Length : {float(self.l)}")
		print(f"Width : {float(self.w)}")
		print(f"Height : {float(self.h)}")
		print(f"Perimeter : {float(self.perimeter())}")
		print(f"Area : {float(self.area())}")
		print(f"Volume : {float(self.volume())}")
		print("=========================\n")
	




box = Rectangle(2, 4)
box.display()

bucket = parallelepipede(7, 5, 6)
bucket.display()

