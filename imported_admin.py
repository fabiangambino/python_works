from users2 import User, Admin, Privileges



fabian = Admin('fabian', 'gambino', 'fabiangambino', 'fabian@f.com', "brooklyn")
fabian.privileges.show_privileges()
fabian.greet_user()