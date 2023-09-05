"""Importing random interger function from random module to generate random dice rolls"""
from random import randint

"""Initializing a Die Class allowing us to create different types of Dices"""
class Die:

	"""The default dice has 6 sides"""
	def __init__(self, sides = 6):
		self.sides = sides

	"""This function returns a random number between and including 1 and the total number of dice sides"""
	def roll_die(self):
		return randint(1, self.sides)

"""Here we make a 6 sided Dice"""
d6 = Die()


"""Here we roll the 6 sided Dice 10 times and print the results"""
print("Here are the results of rolling the 6 sided dice 10 times.")
for roll in range(10):
	print(d6.roll_die())

"""Here we make a 10 sided Dice and a 20 sided Dice"""
d10 = Die(10)
d20 = Die(20)

"""Here we roll the 10 sided Dice 10 Times and the 20 sided Dice 10 Times"""
print("Here are the results of rolling the 10 sided dice 10 times.")
for roll in range(10):
	print(d10.roll_die())

print("Here are the results of rolling the 10 sided dice 10 times.")
for roll in range(10):
	print(d20.roll_die())