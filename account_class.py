class Account:
    # Account class constructor with optional arguments for username, password, firstname and lastname
    def __init__(self, username=None, password=None, firstname=None, lastname=None):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    # returns a list of the Account class object properties to be used for writing to the csv file
    def get_account_details(self):
        return [self.username, self.password, self.lastname, self.firstname]
