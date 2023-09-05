guests =['Jesus', 'Thomas Jefferson', 'Joseph Stalin']

for person in guests:
	print(f"{person}, please accept my invitation to dinner.")

print(f"\n{guests[1]} cannot make the dinner.\n")

guests.remove('Thomas Jefferson')
guests.insert(1, 'George Washington')

for person in guests:
	print(f"{person}, please accept my invitation to dinner.")

print("\nI have found a larger table and have room for more guests.\n")

guests.insert(0, "Alphalpha")
guests.insert(2, "Mediano Italiano")
guests.append("Maximus, General of the Roman Legions")

for person in guests:
	print(f"{person}, please accept my invitation to dinner.")

print("\nI apologize as the larger table has not arrived, and now I can only have two guests.\n")

#print(guests)

first = guests.pop(0)
print(f"I'm sorry {first}, but I can no longer have enough space to invite you to dinner.")
second= guests.pop(-1)
print(f"I'm sorry {second}, but I can no longer have enough space to invite you to dinner.")
third = guests.pop(0)
print(f"I'm sorry {third}, but I can no longer have enough space to invite you to dinner.")
fourth = guests.pop(-1)
print(f"I'm sorry {fourth}, but I can no longer have enough space to invite you to dinner.\n")

for person in guests:
	print(f"{person}, you are still invited!")

del guests[0]
del guests[0]

print(guests)