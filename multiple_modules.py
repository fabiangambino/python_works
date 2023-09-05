from Admin_Priv_Class import Admin, Privileges 

privs = [
	'can delete users',
	'can ban users', 
	'can create users',
	]

fabian = Admin('fabian', 'gambino', 'fabiangambino', 'fabian@f.com', 'brooklyn')
fabian.privileges = Privileges(privs)
fabian.privileges.show_privileges()