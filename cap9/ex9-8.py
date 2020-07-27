class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def show_user(self):
        print("Username: " +self.username)
        print("Password: " +self.password)
    
class Privileges():
    def __init__(self):
        self.privileges = ['ban user', 'delete post', 'add post']
    
    def show_privileges(self):
        for priv in self.privileges:
            print(priv)

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.privileges = Privileges()
    

admin = Admin('hugo', '1234')
admin.show_user()
admin.privileges.show_privileges()