from account_class import Account


# Function to check if the user name and password is valid
# if the user name and password are valid, this function returns the Account object for the username and password
# else, it returns None
def passwd_valid(accounts, user, user_pass):
    # if there are no accounts, return false
    if len(accounts) == 0:
        return None

    # following code loops through the list of accounts
    for account in accounts:
        # check to see if entered username matches the account username
        if user == account.username:
            # check to see if the entered password matches the password for the associated username
            valid_pass = account.password
            if valid_pass == user_pass:
                return account
    return None


# Function to pull up the login screen.
# returns the Account object for the user that logged in
def login_screen(accounts):
    print("Login to your existing account")
    user_found = None
    while user_found is None:  # while loop allows user to keep entering until input is valid
        user = input("Username: ")
        user_pass = input("Password: ")
        user_found = passwd_valid(accounts, user, user_pass)
        if user_found is None:
            print("Incorrect username / password, please try again")
    print("You have successfully logged in as", user_found.username)

    # return the account object for the user that logged in
    return user_found
