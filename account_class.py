class Account:
    def __init__(self, username=None, password=None, firstname=None, lastname=None):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def get_account_details_list(self):
        return [self.username, self.password, self.lastname, self.firstname]
