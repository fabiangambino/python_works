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
