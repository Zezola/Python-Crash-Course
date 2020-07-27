class Privileges():
    def __init__(self):
        self.privileges = ['ban user', 'delete post', 'add post']
    
    def show_privileges(self):
        for priv in self.privileges:
            print(priv)