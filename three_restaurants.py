class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open.")

curry_kitchen = Restaurant('Curry Kitchen', 'Indian')
via_313 = Restaurant('Via 313', 'Italian')
halal_taza = Restaurant('Halal Taza', 'Middle Eastern')

curry_kitchen.describe_restaurant()
via_313.describe_restaurant()
halal_taza.describe_restaurant()

