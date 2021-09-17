import csv


# function to pull up main screen
def main_screen(usernames, passwords):
    print("WELCOME TO InCollege!")
    print("Would you like to create a new account or log into an existing account?")

    # accepts user input and will bring them to the appropriate screen
    user_input = input("(Enter 'n' for new account or 'e' for existing account)")

    if user_input == 'n':
        create_account(usernames, passwords)
    else:
        # will take user to the 'user login' screen
        pass


# function to pull up account creation screen
def create_account(usernames, passwords):
    username_ = " "
    password_ = " "

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
    while username_condition:   # while loop allows user to keep entering until input is valid
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
    while condition:    # while loop allows user to keep entering until input is valid
        password_ = input()

        if len(password_) < 8 or len(password_) > 12:
            print("Error: password must be a minimum of 8 and a maximum of 12 characters")
            continue

        if password_.isalpha():
            print("Error: password must contain at least 1 digit")
            continue

        if password_.isalnum():
            print("Error: password must contain at least 1 non-alpha character")
            continue

        for x in password_:
            if x.isupper():
                condition = False
                break

        if not condition:
            continue
        else:
            print("Error: password must contain at least 1 capital letter")

    # following code updates the database file
    with open('accounts.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        x = 0
        while x < len(usernames):
            csv_writer.writerow([usernames[x], passwords[x]])
            x += 1

        csv_writer.writerow([username_, password_])


# PROGRAM START #
account_usernames = []
account_passwords = []

# following code stores the file contents into lists for later use
with open('accounts.txt', 'r') as read_file:
    csv_reader = csv.reader(read_file, delimiter=',')
    for row in csv_reader:
        account_usernames.append(row[0])
        account_passwords.append(row[1])

main_screen(account_usernames, account_passwords)
