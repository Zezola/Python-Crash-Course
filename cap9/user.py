class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def show_user(self):
        print("Username: " +self.username)
        print("Password: " +self.password)