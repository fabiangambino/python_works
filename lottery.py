from random import choice

lottery_chars = [1,2,3,4,5,6,7,8,9,10, "a", "b", "c", "d"]
winning_chars = []

while len(winning_chars) < 4:
	current_selection = choice(lottery_chars)
	if current_selection not in winning_chars:
		winning_chars.append(current_selection)

print(f"Any ticket matching the characters in {winning_chars} wins a prize.")