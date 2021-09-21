import csv


# Function to check if the user name and password is valid
def passwd_valid(usernames, passwords, user, user_pass):
    for x in usernames:
        if user == x:  # User is found in dataset
            pass_id = usernames.index(x)
            valid_pass = passwords[pass_id]
            if valid_pass == user_pass:
                return True
    return False


# Function to pull up the login screen.
def login_screen(usernames, passwords):
    print("Login to your existing account")
    user_found = False
    while user_found is not True:  # while loop allows user to keep entering until input is valid
        user = input("Username: ")
        user_pass = input("Password: ")
        user_found = passwd_valid(usernames, passwords, user, user_pass)
        if user_found is not True:
            print("Incorrect username / password, please try again")
    print("You have successfully logged in")
    return user_found


# Function to pull up the options menu
def options_screen():
    menu_opt = {"1": "Search for a Job",
                "2": "Find Someone you know",
                "3": "Learn a new skill"}

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
        else:
            print("Unknown Selection, Try Again!")


# function to pull up main screen
def main_screen(usernames, passwords):
    print("WELCOME TO InCollege!")
    print("Would you like to create a new account or log into an existing account?")

    # accepts user input and will bring them to the appropriate screen
    logged_in = False
    main_condition = True

    while main_condition:
        user_input = input("(Enter 'n' for new account or 'e' for existing account)")

        if user_input == 'n':
            main_condition = False
            create_account(usernames, passwords)
            logged_in = login_screen(usernames, passwords)
        elif user_input == 'e':
            main_condition = False
            logged_in = login_screen(account_usernames, account_passwords)
        else:
            print("Please enter 'n' or 'e'")

    if logged_in:
        options_screen()


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
def create_account(usernames, passwords):
    username_ = " "
    password_ = " "
    lastname_ = " "
    firstname_ = " "

    # following code checks if there are 5 stored passwords already
    line_count = 0
    for name in usernames:
        line_count += 1

    if line_count == 5:
        print("All permitted accounts have been created, please come back later")
        return

    # following code allows user to create a username and validates that it is unique
    print("Enter the username you wish to use:")

    username_condition = True
    while username_condition:  # while loop allows user to keep entering until input is valid
        exit_loop = False
        username_ = input()

        for x in usernames:
            if username_ == x:
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

    condition = True
    while condition:  # while loop allows user to keep entering until input is valid
        password_ = input()
        condition, message = is_secure(password_)
        if not condition:
            print(message)
            continue
        else:
            break

    # following code allows the user to save their first and last name
    print("Enter your first name:")
    firstname_ = input()

    print("Enter your last name: ")
    lastname_ = input()

    # following code updates the database file
    with open('accounts.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        x = 0
        while x < len(usernames):
            csv_writer.writerow([usernames[x], passwords[x]])
            x += 1

        csv_writer.writerow([username_, password_, lastname_, firstname_])

    account_usernames.append(username_)
    account_passwords.append(password_)
    account_lastnames.append(lastname_)
    account_firstnames.append(firstname_)

    print("You've Successfully created an account!\n")


# PROGRAM START #
account_usernames = []
account_passwords = []
account_lastnames = []
account_firstnames = []

# following code stores the file contents into lists for later use
with open('accounts.txt', 'r') as read_file:
    csv_reader = csv.reader(read_file, delimiter=',')

    num_lines = len(list(csv_reader))

    if num_lines == 0:
        pass
    else:
        for row in csv_reader:
            account_usernames.append(row[0])
            account_passwords.append(row[1])
            account_lastnames.append(row[2])
            account_firstnames.append(row[3])

if __name__ == '__main__':
    main_screen(account_usernames, account_passwords)
