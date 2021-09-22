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

    # the eq operator function runs when an object is compared using the == operator
    def __eq__(self, other):
        # the object being compare to is a tuple
        if type(other) == tuple:
            # the tuple has 2 items
            if len(other) == 2:
                # following code converts the tuple to a list and then checks to see if
                # the items in the list contain the account object's first and last name
                other_list = list(other)
                if self.firstname in other_list:
                    # remove the first name from the list for the in case
                    # an account has the same first and last name
                    other_list.remove(self.firstname)
                    if self.lastname in other_list:
                        return True
                return False

