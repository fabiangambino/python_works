from random import choice

# A list of lottery numbers ranging from 1 to 32 inclusive.
lottery_numbers = [x for x in range(1, 32)]

# A function that asks user to input 4 numbers within a specific range and handles edge cases
def select_ticket_numbers():
	my_ticket = []
	while len(my_ticket) < 4:
		number = input("Please select a number from 1 through 32: ")
		try: 
			number = int(number)
			if number > max(lottery_numbers) or number < min(lottery_numbers):
				print('    Error: "Outside of Range! You can only select numbers between 1 and 32."')
			elif number in my_ticket:
				print('    Error: "You cannot pick the same number multiple times. Try again."')
			else:
				my_ticket.append(number)
		except ValueError:
			print('    Error: "Please enter numbers only."')
	return my_ticket


# A function that uses a list of numbers to generate 4 winning lottery numbers for a drawing
def generate_winning_numbers(lottery_numbers):
	winning_numbers = []
	while len(winning_numbers) < 4:
		current_number = choice(lottery_numbers)
		if current_number not in winning_numbers:
			winning_numbers.append(current_number)
	return winning_numbers

# A function that checks that every number in my_ticket is one of the winning_numbers.
def did_win(my_ticket, winning_numbers):
	for num in my_ticket:
		if num not in winning_numbers:
			return False
	return True 

# TODO MODIFY LOOP TO NOT BE INFINITE
def times_to_win(my_ticket):
	winning_numbers = generate_winning_numbers(lottery_numbers)
	counter = 1
	while True:
		if did_win(my_ticket, winning_numbers) == False:
			winning_numbers = generate_winning_numbers(lottery_numbers)
			counter += 1
		elif did_win(my_ticket, winning_numbers) == True:
			print(f"Winning Numbers:\n{winning_numbers}")
			print(f"My Numbers:\n{my_ticket}")
			print(f"It took playing {counter} games with your numbers to win.")
			break


#User is prompted to select numbers
my_ticket = select_ticket_numbers()
#User's ticket is displayed
times_to_win(my_ticket)



