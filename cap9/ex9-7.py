class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def show_user(self):
        print("Username: " +self.username)
        print("Password: " +self.password)
    

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.privileges = ['ban user', 'delete post', 'add post']
    
    def show_privileges(self):
        print("Admin's privileges: \n")
        for priv in self.privileges:
            print(priv)

admin = Admin('hugo', '1234')
admin.show_user()
admin.show_privileges()