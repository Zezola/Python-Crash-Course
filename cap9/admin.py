from user import User 
from priv import Privileges


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.privileges = Privileges()