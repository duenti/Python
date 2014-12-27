class Parent():
	def __init__(self,last_name,eye_color):
		print("Construtor Pai chamado")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)

class Child(Parent):
	def __init__(self,last_name,eye_color,number_toys):
		print("Construtor filho chamado")
		Parent.__init__(self,last_name,eye_color)
		self.number_toys = number_toys

	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)
		print("Number of toys - " + self.number_toys)

billy_cyrus = Parent("Cyrus","blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus","blue",5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_toys)