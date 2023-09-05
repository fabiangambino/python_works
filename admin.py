class User:

	def __init__(self, first_name, last_name, phone_number, email_address):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number
		self.email_address = email_address

	def describe_user(self):
		print(f"User's Name: {self.first_name.title()} {self.last_name.title()}")
		print(f"Phone Number: {self.phone_number}")
		print(f"Email Address: {self.email_address}\n")

	def greet_user(self):
		print(f"Welcome, {self.first_name.title()} {self.last_name.title()}.\n")

class Admin(User):

	def __init__(self, first_name, last_name, phone_number, email_address):
		super().__init__(first_name, last_name, phone_number, email_address)
		self.priveleges = []

	def show_priveleges(self):
		print("Admin Priveleges:\n")
		for privelege in self.priveleges:
			print(privelege.title())

fabian = Admin('Fabian', 'Gambino', '123-123-1234', 'fabian@f.com')
fabian.describe_user()

fabian.priveleges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts',
	]

fabian.show_priveleges()


