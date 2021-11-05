# import pytest
from important_links import important_links_groups, guest_controls, update_guest_controls, account_language, \
    update_account_language
from profile_creation import *
from search_students import *
from pending_requests import *
from show_network import *
from useful_links import useful_links_groups
from account_creation import create_account, is_secure
from job_creation import create_job
from job_deletion import *
from job_apply import apply_job
from account_login import passwd_valid, login_screen
from csv_read_write import get_accounts_from_csv, get_jobs_from_csv
from send_message import send_message_ui
from view_message import at_least_1_new_message, view_messages_ui
from notifications import *
from csv_read_write import get_jobs_from_csv
from job_apply import count_applied_job


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
            print("\t", x, ")", menu[x])
        selection = input("\t Choose an option:")
        if selection == '1':
            print("\nVideo is now Playing.\n")
            input("Press Enter to exit\n")
        elif selection == '2':
            break
        else:
            print("Unknown Selection, Try Again!")


# function to pull up main screen
def main_screen(accounts, jobs=None):
    print("\nWELCOME TO InCollege!")
    main_screen_opt = {"1": "Create a new account",
                       "2": "Login to existing account",
                       "3": "Connect with friends",
                       "4": "InCollege Useful Links",
                       "5": "InCollege Important Links",
                       "q": "Quit InCollege"}

    # accepts user input and will bring them to the appropriate screen
    logged_in_user = None
    main_condition = True

    while main_condition:
        # following code handles the user input for the main screen
        options = main_screen_opt.keys()
        for x in options:
            print(x, ")", main_screen_opt[x])
        selection = input("Select an Option: ")

        if selection == '1':
            main_condition = False
            create_account(accounts)
            logged_in_user = login_screen(accounts)
        elif selection == '2':
            main_condition = False
            logged_in_user = login_screen(accounts)
        elif selection == '3':
            # if the user is able to connect with an existing account, they are given the option to login or sign up
            if connect_with_users(accounts):
                print("\nWould you like to login or sign up to join your friend?")
                connected_condition = True

                while connected_condition:
                    connected_selection = input("(Enter 'l' to login, 's' for sign up or 'q' to go back): ")
                    if connected_selection == 'l':  # user selected login
                        connected_condition = False
                        logged_in_user = login_screen(accounts)
                        main_condition = not logged_in_user
                    elif connected_selection == 's':  # user selected sign up
                        connected_condition = False
                        create_account(accounts)
                        logged_in_user = login_screen(accounts)
                        main_condition = not logged_in_user
                    elif connected_selection == 'q':  # user selected go back
                        connected_condition = False
                    else:
                        print("\nUnknown Selection, Try Again!\n")
        elif selection == '4':
            # if the user selected signup from the useful links general group
            # go to the create account screen
            signup_selected = useful_links_groups()
            if signup_selected:
                main_condition = False
                create_account(accounts)
                logged_in_user = login_screen(accounts)
        elif selection == '5':
            important_links_groups(False)
        elif selection == 'q':
            main_condition = False
            print("\nHave a nice day!")
        else:
            print("\nUnknown Selection, Try Again!\n")

    if logged_in_user is not None:
        options_screen(logged_in_user, accounts, jobs)


# Function to pull up the options menu
# The user argument is the Account object for the user that is logged in
# The accounts argument is the accounts list
# The jobs argument is the jobs list
def options_screen(user, accounts, jobs):
    # Determines if the logged in user has any pending friend requests and notifies them if so

    # requests = at_least_1_pending(user)
    # if requests > 0:
    #     print("\n*** YOU HAVE PENDING FRIEND REQUESTS! CHOOSE OPTION 9 FOR MORE INFO! ***")

    # determine if the logged in user has any new messages and notifies them if so
    num_messages = at_least_1_new_message(user)
    if num_messages > 0:
        print("\n*** YOU HAVE NEW MESSAGES! CHOOSE OPTION 11 FOR MORE INFO! ***")

    # show notifications on login
    login_notifications = get_login_notifications(user)
    print("\n ********* Notifications(", len(login_notifications), ") ********* \n", sep="")
    for notification in login_notifications:
        print(" *", notification)

    menu_opt = {"1": "Job Search/Internship",
                "2": "Find Someone you know",
                "3": "Learn a new skill",
                "4": "InCollege Useful Links",
                "5": "InCollege Important Links",
                "6": "Create Profile",
                "7": "View Profile",
                "8": "Search Students",
                "9": "Pending Friend Requests",
                "10": "Show My Network",
                "11": "Messaging",
                "q": "Logout and Quit InCollege"}

    menu_skills = {"1": "Communication",
                   "2": "Software",
                   "3": "Marketing",
                   "4": "Project Management",
                   "5": "Design",
                   "q": "Quit"}

    menu_jobs = {"1": "Post a Job",
                 "2": "View Job Listings",
                 "3": "Delete a Job You Posted",
                 "q": "Quit"}

    menu_messaging = {"1": "Send a Message",
                      "2": "View Messages",
                      "q": "Quit"}

    while True:
        print("\n ********* InCollege Options ********* \n")

        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")
        if selection == '1':
            # Pulls up the menu with options for jobs
            while True:
                # Determines how many jobs the user has applied for and notifies them if so
                if count_applied_job(user) > 0:
                    applied_count = count_applied_job(user)
                    print("\n*** You have applied for ", applied_count, "jobs. ***")

                # Determines if any jobs that the user has applied for have been deleted and notifies them if so
                jobs_deleted = user_job_deleted(user)
                if jobs_deleted:
                    print("\n *** ATTENTION: A JOB YOU APPLIED FOR HAS BEEN DELETED! ***")

                print("\n ********* Job Options ********* \n")

                options = menu_jobs.keys()
                for x in options:
                    print(x, ")", menu_jobs[x])

                selection = input("Select an Option: ")
                if selection == '1':
                    create_job(user, jobs)
                elif selection == '2':
                    apply_job(user, jobs)

                elif selection == '3':
                    delete_job(user, jobs)
                elif selection == 'q':
                    break
                else:
                    print("Unknown selection! Try Again!")

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
        elif selection == '4':
            while useful_links_groups():
                print("\nYou are already signed in, please sign out to create a new account")
        elif selection == '5':
            important_links_groups(user, accounts)
            print("return to main options links")
            for account in accounts:
                print(account.get_account_details())
        elif selection == '6':
            profile_creation(user)
        elif selection == '7':
            view_profile()
        elif selection == '8':
            search_students(user, accounts)
        elif selection == '9':
            pending_requests(user, accounts)
        elif selection == '10':
            show_network(user)
        elif selection == '11':
            while True:
                # print messaging menu
                print("\n ********* Messaging Options ********* \n")

                options = menu_messaging.keys()
                for x in options:
                    print(x, ")", menu_messaging[x])

                messaging_selection = input("Select an Option: ")
                if messaging_selection == '1':
                    send_message_ui(user, accounts)
                elif messaging_selection == '2':
                    view_messages_ui(user, accounts)
                elif messaging_selection == 'q':
                    break
                else:
                    print("Unknown Selection, Try Again!")


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


# PROGRAM START #
accounts_list = []  # global variable that holds all of the account objects
jobs_list = []  # global variable that holds all of the job objects
if __name__ == '__main__':
    accounts_list = get_accounts_from_csv()
    jobs_list = get_jobs_from_csv()

    home_screen()
    main_screen(accounts_list, jobs_list)
