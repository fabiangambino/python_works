class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is currently open.")

	def set_number_served(self, customers_served):
		self.number_served = customers_served

restaurant = Restaurant('Curry Kitchen', 'Indian')

print(f"{restaurant.number_served}")
restaurant.number_served = 5
print(f"{restaurant.number_served}")
restaurant.set_number_served(15)
print(f"{restaurant.number_served}")
