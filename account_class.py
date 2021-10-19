class Account:
    # Account class constructor with optional arguments for username, password, firstname and lastname
    def __init__(self, username=None, password=None, firstname=None, lastname=None, incollege_email=None, sms=None, targeted_ads=None, language=None):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.num_applied = 0

        # logic for account controls defaults
        if incollege_email is None:
            # default on account creation
            self.incollege_email = True
        elif incollege_email == "True":
            self.incollege_email = True
        elif incollege_email == "False":
            self.incollege_email = False
        else:
            # default if true or false not passed as the constructor argument
            self.incollege_email = True
            
        if sms is None:
            self.sms = True
        elif sms == "True":
            self.sms = True
        elif sms == "False":
            self.sms = False
        else:
            self.sms = True
    
        if targeted_ads is None:
            self.targeted_ads = True
        elif targeted_ads == "True":
            self.targeted_ads = True
        elif targeted_ads == "False":
            self.targeted_ads = False
        else:
            self.targeted_ads = True
            
        if language is None:
            self.language = "English"
        elif language == "English":
            self.language = "English"
        elif language == "Spanish":
            self.language = "Spanish"
        else:
            self.language = "English"

    # returns a list of the Account class object properties to be used for writing to the csv file
    def get_account_details(self):
        return [self.username, self.password, self.firstname, self.lastname, self.incollege_email, self.sms, self.targeted_ads, self.language]

    # returns a list of the Account class object properties for the guest controls
    def get_account_controls(self):
        return [self.incollege_email, self.sms, self.targeted_ads]
