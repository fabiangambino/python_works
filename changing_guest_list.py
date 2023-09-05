guests =['Jesus', 'Thomas Jefferson', 'Joseph Stalin']  
for person in guests:
	print(f"{person}, please accept my invitation to dinner.")
print(f"{guests[1]} cannot make the dinner.")
guests.remove('Thomas Jefferson')
guests.insert(1, 'George Washington')
for person in guests:
	print(f"{person}, please accept my invitation to dinner.")