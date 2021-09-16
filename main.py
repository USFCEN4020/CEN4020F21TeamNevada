# function to pull up main screen
def main_screen():
    print("WELCOME TO InCollege!")
    print("Would you like to create a new account or log into an existing account?")

    # accepts user input will bring them to the appropriate screen
    user_input = input("(Enter 'n' for new account or 'e' for existing account)")

    if user_input == 'n':
        # print("call create account function")
        create_account()
    else:
        print("user login screen")


# function to pull up account creation screen
def create_account():
    username_ = input("Enter the username you wish to use:")
    # eventually will check database(file) to make sure username is unique (via 'if' condition)

    # allows user to create a password and validates input with the given conditions
    condition = True
    while condition:
        print("Enter the password you wish to user. Your password must contain: \n",
        "a minimum of 8 characters\n",
        "a maximum of 12 characters\n",
        "at least one capital letter\n",
        "at least one digit\n",
        "at least one non-alphabetic character")
        password_ = input()

        if len(password_) < 8 or len(password_) > 12:
            continue

        if not password_.isalnum():
            continue


# PROGRAM START #
main_screen()
