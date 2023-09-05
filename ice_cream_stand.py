class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open.")

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'vanilla', 'strawberry']

	def display_flavors(self):
		print(f"Flavors:\n")
		for flavor in self.flavors:
			print(flavor.title())  

parlor = IceCreamStand("Jack's Ice Cream Parlor", "Comfort")
parlor.display_flavors()
