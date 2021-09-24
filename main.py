import csv
from account_class import Account
from job_class import Job


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
        print_menu(menu)
        selection = input("Choose an option:")
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
    return user_found, user # returns a login confirmation and username of logged-in user


# Function to pull up the options menu
def options_screen(user):
    menu_opt = {"1": "Search for a Job",
                "2": "Find Someone you know",
                "3": "Learn a new skill"}
    menu_skills = {"1": "Communication",
                   "2": "Software",
                   "3": "Marketing",
                   "4": "Project Management",
                   "5": "Design",
                   "q": "Quit"}
    menu_jobs = {"1": "Post a Job",
                 "2": "View Job Listings",
                 "q": "Quit"}
    while True:
        print("\n ********* InCollege Options ********* \n")

        print_menu(menu_opt)
        selection = input("Select an Option: ")
        # Selection for "Search for a Job"
        if selection == '1':
            while True:
                print_menu(menu_jobs)
                selection = input("Select an Option: ")
                # Post a Job
                if selection == '1': 
                    create_job(user)
                # View Job Listings
                elif selection == '2':
                    print("\n Under Construction!\n")
                # Quit
                elif selection == 'q':
                    break
                else:
                    print("Unknown Selection, Try Again!")
        # Selection for "Find Someone you know"
        elif selection == '2':
            print("\nUnder Construction\n")
        # Selection for "Learn a new skill"
        elif selection == '3':
            while True:
                print("\n ********* Learn a Skill! ********* \n")
                print_menu(menu_skills)
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
def main_screen(accounts):

    print("\nWould you like to create a new account or log into an existing account?")

    # accepts user input and will bring them to the appropriate screen
    logged_in = False
    main_condition = True

    while main_condition:
        user_input = input("(Enter 'n' for new account or 'e' for existing account): ")

        if user_input == 'n':
            main_condition = False
            create_account(accounts)
            logged_in, user = login_screen(accounts)
        elif user_input == 'e':
            main_condition = False
            logged_in, user = login_screen(accounts)
        else:
            print("Please enter 'n' or 'e'")

    if logged_in:
        options_screen(user)


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

# Function to create job posting 
def create_job(user):

    title_ = " "
    description_ = " "
    employer_ = " "
    salary_ = " "

    # checks for 5 stored jobs listings
    line_count = len(jobs_list)
    if line_count >= 5:
        print("The listing limit has been reached. Only 5 jobs are permitted to be posted at a time.")
        return
    title_ = input("Job Title:")
    description_ = input("Job Description:")
    employer_ = input("Job Employer:")
    salary_ = input("Job Salary:")

    # following code creates a job object to "post" a Job
    created_job_ = Job(user, title_, description_, employer_, salary_)
    jobs_list.append(created_job_)

    # following code updates the database file
    with open('jobs.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # loops through the accounts and writes them to the csv file
        for job in jobs_list:
            csv_writer.writerow(job.get_job_details())

    print("Your Job was posted successfully!\n")


    return

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

# Helpful Function to print a Dictionary-based menu.
def print_menu(menu):
    options = menu.keys()
    for x in options:
        print(x, ")", menu[x])   

# PROGRAM START #
accounts_list = []  # global variable that holds all of the account objects
jobs_list = [] # global variable that holds a list of job objects
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

    # following code reads the csv file and stores the jobs listings
    with open('jobs.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            # stores the data from the csv file to the job list
            for row in csv_reader:
                jobs_list.append(Job(row[0], row[1], row[2], row[3], row[4]))
        except IndexError:  # handles the error if the csv file is empty
            pass

    home_screen()
    main_screen(accounts_list)
