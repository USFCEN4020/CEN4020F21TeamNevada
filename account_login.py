from account_class import Account


# Function to check if the user name and password is valid
def passwd_valid(accounts, user, user_pass):
    # if there are no accounts, return false
    if len(accounts) == 0:
        return False

    # following code loops through the list of accounts
    for account in accounts:
        # check to see if entered username matches the account username
        if user == account.username:
            # check to see if the entered password matches the password for the associated username
            valid_pass = account.password
            if valid_pass == user_pass:
                return True
    return False


# Function to pull up the login screen.
def login_screen(accounts):
    print("Login to your existing account")
    user_found = False
    while user_found is not True:  # while loop allows user to keep entering until input is valid
        user = input("Username: ")
        user_pass = input("Password: ")
        user_found = passwd_valid(accounts, user, user_pass)
        if user_found is not True:
            print("Incorrect username / password, please try again")
    print("You have successfully logged in")
    return user_found