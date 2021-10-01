import csv
#import pytest
from account_class import Account
from important_links import important_links_groups

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

# Function for the HomeScreen
def home_screen():

    # "Homepage" Menu
    menu = {"1": "Welcome Video",
            "2": "Login/Register"}

    print("\t***************************\n\t   Welcome to InCollege!\n\t***************************\n")
    print("\t   ** Success Story! **\n")
    print("\t   Daniela, USF 21':\n \"InCollege has made my stressful job search a\n thousands times",
          "easier by connecting with other\n students and applying to jobs in one go!\"\n")

    while True:
        # prints menu options
        options = menu.keys()
        for x in options:
            print("\t",x, ")", menu[x]) 
        selection = input("\t Choose an option:")
        if selection == '1':
            print("\nVideo is now Playing.\n")
            input("Press Enter to exit\n")
        elif selection == '2':
            break
        else:
            print("Unknown Selection, Try Again!")


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


# Function to pull up the options menu
def options_screen(accounts):
    menu_opt = {"1": "Search for a Job",
                "2": "Find Someone you know",
                "3": "Learn a new skill",
                "5": "InCollege Important Links",
                "q": "Logout and Quit InCollege"}

    menu_skills = {"1": "Communication",
                   "2": "Software",
                   "3": "Marketing",
                   "4": "Project Management",
                   "5": "Design",
                   "q": "Quit"}

    while True:
        print("\n ********* InCollege Options ********* \n")

        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")
        if selection == '1':
            print("\nUnder Construction\n")
        elif selection == '2':
            # connect_with_users(accounts)
            print("\nUnder Construction\n")
        elif selection == '3':
            while True:
                print("\n ********* Learn a Skill! ********* \n")

                skills = menu_skills.keys()
                for x in skills:
                    print(x, ")", menu_skills[x])

                selection = input("Select a skill: ")
                if selection == '1':
                    print("\nUnder Construction\n")
                elif selection == '2':
                    print("\nUnder Construction\n")
                elif selection == '3':
                    print("\nUnder Construction\n")
                elif selection == '4':
                    print("\nUnder Construction\n")
                elif selection == '5':
                    print("\nUnder Construction\n")
                elif selection == 'q':
                    break
                else:
                    print("Unknown Selection, Try Again!")
        elif selection == '5':
            signup_selected = important_links_groups()
        elif selection == 'q':
            print("\nHave a nice day!")
            break
        else:
            print("Unknown Selection, Try Again!")


# Function to connect with other users
def connect_with_users(accounts):
    # following code gets the first and last name of the user to search for
    print("\n ********* Connect with other InCollege users ********* \n")
    firstname_ = input("Enter the person's first name: ")
    lastname_ = input("Enter the person's last name: ")

    if user_exists(accounts, firstname_, lastname_):
        print("\nThey are a part of the InCollege system!")
        return True
    else:
        print("\nThey are not yet part of the InCollege system!")
        return False


# function looks to see if there is an account with the a matching first and last name
def user_exists(accounts, firstname, lastname):
    # loop through the accounts
    for account in accounts:
        if account.firstname == firstname and account.lastname == lastname:
            return True

    return False


# function to pull up main screen
def main_screen(accounts):
    print("WELCOME TO InCollege!")
    main_screen_opt = {"1": "Create a new account",
                "2": "Login to existing account",
                "3": "Connect with friends",
                "5": "InCollege Important Links",
                "q": "Quit InCollege"}

    # accepts user input and will bring them to the appropriate screen
    logged_in = False
    main_condition = True

    while main_condition:
        # following code handles the user input for the main screen
        print("Would you like to create a new account, log into an existing account or connect with friends?")
        options = main_screen_opt.keys()
        for x in options:
            print(x, ")", main_screen_opt[x])
        selection = input("Select an Option: ")

        if selection == '1':
            main_condition = False
            create_account(accounts)
            logged_in = login_screen(accounts)
        elif selection == '2':
            main_condition = False
            logged_in = login_screen(accounts)
        elif selection == '3':
            # if the user is able to connect with an existing account, they are given the option to login or sign up
            if connect_with_users(accounts):
                print("\nWould you like to login or sign up to join your friend?")
                connected_condition = True

                while connected_condition:
                    connected_selection = input("(Enter 'l' to login, 's' for sign up or 'q' to go back): ")
                    if connected_selection == 'l':  # user selected login
                        connected_condition = False
                        logged_in = login_screen(accounts)
                        main_condition = not logged_in
                    elif connected_selection == 's':  # user selected sign up
                        connected_condition = False
                        create_account(accounts)
                        logged_in = login_screen(accounts)
                        main_condition = not logged_in
                    elif connected_selection == 'q':  # user selected go back
                        connected_condition = False
                    else:
                        print("\nUnknown Selection, Try Again!\n")
        elif selection == '5':
            signup_selected = important_links_groups()
        elif selection == 'q':
            main_condition = False
            print("\nHave a nice day!")
        else:
            print("\nUnknown Selection, Try Again!\n")

    if logged_in:
        options_screen(accounts)


# Function to check if a password is secure, a secure password should contain
# minimum of 8 characters, maximum of 12 characters, at least one capital letter, one
# digit, one non-alpha character
def is_secure(passwd):
    if not 8 <= len(passwd) <= 12:
        return False, 'Error: password must be a minimum of 8 and a maximum of 12 characters'
    contain_capital = False
    contain_digit = False
    contain_non_alpha = False
    for c in passwd:
        # check if c is a capital letter
        if c.isalpha() and c.upper() == c:
            contain_capital = True
        # check if c is a digit
        if c.isdigit():
            contain_digit = True
        # check if c is a non-alpha character
        if not c.isalpha():
            contain_non_alpha = True
    if not contain_digit:
        return False, "Error: password must contain at least 1 digit"
    if not contain_capital:
        return False, "Error: password must contain at least 1 capital letter"
    if not contain_non_alpha:
        return False, "Error: password must contain at least 1 non-alpha character"
    return True, ''


# function to pull up account creation screen
def create_account(accounts):
    username_ = " "
    password_ = " "
    lastname_ = " "
    firstname_ = " "

    # following code checks if there are 5 stored passwords already
    line_count = len(accounts)
    if line_count >= 5:
        print("All permitted accounts have been created, please come back later")
        return

    # following code allows user to create a username and validates that it is unique
    print("Enter the username you wish to use:")

    username_condition = True
    while username_condition:  # while loop allows user to keep entering until input is valid
        exit_loop = False
        username_ = input()

        for x in accounts:
            if username_ == x.username:
                print("Error: entered username is taken. enter another username")
                exit_loop = True
                break

        if not exit_loop:
            username_condition = False

    # following code allows user to create a password and validates input with the given conditions
    print("Enter the password you wish to use. Your password must contain: \n",
          "a minimum of 8 characters\n",
          "a maximum of 12 characters\n",
          "at least one capital letter\n",
          "at least one digit\n",
          "at least one non-alphabetic character")

    password_secure = False
    while not password_secure:  # while loop allows user to keep entering until input is valid
        password_ = input()
        password_secure, message = is_secure(password_)
        if not password_secure:
            print(message)

    # following code allows the user to save their first and last name
    print("Enter your first name:")
    firstname_ = input()

    print("Enter your last name: ")
    lastname_ = input()

    # following code creates an account object for the newly created account
    created_account_ = Account(username_, password_, firstname_, lastname_)
    accounts.append(created_account_)

    # following code updates the database file
    with open('accounts.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # loops through the accounts and writes them to the csv file
        for account in accounts:
            csv_writer.writerow(account.get_account_details())

    print("You've Successfully created an account!\n")


# PROGRAM START #
accounts_list = []  # global variable that holds all of the account objects
if __name__ == '__main__':
    # following code reads the csv file and stores the accounts
    with open('accounts.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            # stores the data from the csv file to the accounts list
            for row in csv_reader:
                accounts_list.append(Account(row[0], row[1], row[2], row[3]))
        except IndexError:  # handles the error if the csv file is empty
            pass

    home_screen()
    main_screen(accounts_list)
