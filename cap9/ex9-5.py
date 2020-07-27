class User():
    def __init__(self, username, password):
        ''' Init the attributes values '''
        self.username = username
        self.password = password
        self.login_attempts = 0

    
    def set_login_attempts(self, number):
        ''' Set the value of login_attemps to an specific number'''
        self.login_attempts = number

    
    def add_login_attempts(self):
        ''' Increment the value of login_attempts by one '''
        self.login_attempts += 1
    

    def reset_login_attempts(self):
        self.login_attempts = 0
    

    def get_user_info(self):
        ''' prints information about the user '''
        print("Name: " +self.username)
        print("Password: " +self.password)
        print("Login attempts: " +str(self.login_attempts))
    

user1 = User('mariana', '1234mari')

# Setando o valor de login_attemps pra 20
user1.set_login_attempts(20)

# Incrementando 1 a ele 5 vezes
user1.add_login_attempts()
user1.add_login_attempts()
user1.add_login_attempts()
user1.add_login_attempts()
user1.add_login_attempts()

user1.get_user_info()

# Now reseting the number of login_attempts
user1.reset_login_attempts()

# Printing the user again
user1.get_user_info()