class User:

	def __init__(self, first_name, last_name, phone_number, email_address):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number
		self.email_address = email_address
		self.login_attempts = 0

	def describe_user(self):
		print(f"User's Name: {self.first_name.title()} {self.last_name.title()}")
		print(f"Phone Number: {self.phone_number}")
		print(f"Email Address: {self.email_address}\n")

	def greet_user(self):
		print(f"Welcome, {self.first_name.title()} {self.last_name.title()}.\n")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

bob = User('bob', 'blafford', '123-123-1234', 'bob@b.com')
print(bob.login_attempts)
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
print(bob.login_attempts)
bob.reset_login_attempts()
print(bob.login_attempts)

