from account_class import Account
from csv_read_write import save_accounts_to_csv


def important_links_groups(user=None, accounts=None):
    # Prints the InCollege important Links menu
    menu_opt = {"1": "Copyright Notice",
                "2": "About",
                "3": "Accessibility",
                "4": "User Agreement",
                "5": "Privacy Policy",
                "6": "Cookie Policy",
                "7": "Copyright Policy",
                "8": "Brand Policy",
                "9": "Guest Controls",
                "10": "Languages",
                "q": "Return to home screen"}
    while True:
        print("\n********* Important Link Groups ********* \n")
        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")
        if selection == '1':
            _by_ = "University of South Florida"
            _Author_ = "Lyle Hanner, Yinet Juvier, Dongni Jiang, Nicolas Hernandez, Kameron Ingraham"
            _copyright_ = "Copyright (C) 2021"
            _licence_ = "Public Domain"
            _version_ = "1.0"
            print("********* Copyright Notice *********")
            print("\n",_by_,"\n",_Author_,"\n", _copyright_,"\n", _licence_,"\n", _version_,"\n")
        elif selection == '2':
            print("********* About *********"
                  "\n", "In College: Welcome to In College, the world's largest college student network ",
                  "\n", "with many users in many countries and territories worldwide")
        elif selection == '3':
            print("********* Accessibility *********",
                  "\n", "It is our pleasure to make accessibility and inclusive design part of our main principles, ",
                  "\n", "building accessibility and testing our products to make sure that everyone can use InCollege")
        elif selection == '4':
            print("********* User Agreement *********"
                  ,"\n", "Contract:"
                  ,"\n", "When you use our Services, you agree to all our terms."
                  ,"\n", "You agree that by clicking “Sign Up” or similar, registering, accessing or using our services, "
                  ,"\n", "you are agreeing to enter into a legally binding contract with InCollege. If you do not agree to "
                  ,"\n", "this contract ,do not click “Sign Up” (or similar) and do not access or otherwise use any of our "
                  ,"\n", "Services. If you wish to terminate this contract, at any time you can do so by closing your account "
                  ,"\n", "and no longer accessing or using our Services."
                  ,"\n", "Content:"
                  ,"\n", "We respect the intellectual property rights of others. We require that information posted by "
                  ,"\n", "Members be accurate and not in violation of the intellectual property rights or other rights of"
                  ,"\n", "third parties.")
        elif selection == '5':
            print("********* Privacy Policy *********"
                  ,"\n","You have choices about the information on your profile, like your level of education, skills, photo, "
                  ,"\n","current school, city or area and endorsements. You don’t have to provide additional information on your "
                  ,"\n","profile. It’s your choice whether to include sensitive information on your profile and to make that "
                  ,"\n","sensitive information public. Please do not post or add personal data to your profile that you would not"
                  ,"\n","want to be publicly available.")
        elif selection == '6':
            print("********* Cookie Policy  *********"
                  ,"\n","At InCollege, we believe in being clear and open about how we collect and use data related to you. This Cookie "
                  ,"\n","Policy applies to any InCollege product or service that links to this policy or incorporates it by reference. "
                  ,"\n","We use cookies and similar technologies such as pixels, local storage and mobile ad IDs (collectively referred "
                  ,"\n","to in this policy as “cookies”) to collect and use data as part of our Services.")
        elif selection == '7':
            print("********* Copyright Policy *********"
                  ,"\n","InCollege respects the intellectual property rights of others and desires to offer a platform which contains no content "
                  ,"\n","that violates those rights. Our User Agreement requires that information posted by Members be accurate, lawful and not "
                  ,"\n","in violation of the rights of third parties. "
                  ,"\n","It is our policy, in appropriate circumstances and in our discretion, to disable and/or terminate the accounts of Members, "
                  ,"\n","or groups as the case may be, who infringe or repeatedly infringe the rights of others or otherwise post unlawful content.")
        elif selection == '8':
            print("********* Brand Policy *********"
                  ,"\n","InCollege does not usually permit its members, organizations or individuals to use its name, trademarks, logos, web pages, "
                  ,"\n","screenshots nor other brand features. To be able to use it, members or organizations must obtain prior approval from CollegeIn.")
        elif selection == '9':
            # if the user is signed in, they are allow to adjust the guest controls
            if user is None or accounts is None:
                print("You must be signed in to your InCollege account to access Guest Controls")
            else:
                # account controls
                guest_controls(user, accounts)
                print("return to important links")
                for account in accounts:
                    print(account.get_account_details())
        elif selection == '10':
            account_language(user, accounts)
        elif selection == 'q':
            print("\n")
            break
        else:
            print("Invalid Selection, Try Again!")


# this function handles the guest controls options
def guest_controls(user, accounts):
    menu_opt = {"1": "InCollege Email:",
                "2": "SMS:",
                "3": "Targeted Advertising:",
                "e": "Enable All",
                "d": "Disabled All",
                "q": "Return to important links"}
    menu_condition = True
    changes = False

    while menu_condition:
        # get the logged in account's controls
        account_controls_settings = user.get_account_controls()

        # print the options and controls
        print("\n********* Guest Controls *********\n")
        options = menu_opt.keys()
        for x in options:
            # if the menu item is a control, print the value for the control state as enabled or disabled
            try:
                # the following code tries to get the value of the control state from the list
                # using some clever logic with the int() function and the fact that the menu
                # keys are numbers, and then saves the control state as a string
                control_state = account_controls_settings[int(x)-1]
                control_state_string = "Enabled" if control_state else "Disabled"
                print("{0} ) {1:<25}{2}".format(x, menu_opt[x], control_state_string))
                # print(x, ")", menu_opt[x], control_state_string)
            except ValueError:
                # this error will catch the menu options that are not control states and print the menu option
                print(x, ")", menu_opt[x])

        selection = input("Select an Option to toggle a control, change all controls or save changes: ")

        # if the user opts to change any of the controls, we need to change the
        # quit menu option text and save the changes to the csv once the user is
        # done making changes

        if selection == "q":
            if changes:
                # since user is a reference to the object in the accounts list, we don't have to change the accounts list
                save_accounts_to_csv(accounts)

                print("Saving changes to Guest Controls")
            menu_condition = False
        elif selection in options:
            update_guest_controls(selection, user)
            menu_opt["q"] = "Save changes and return to important links"
            changes = True
        else:
            print("Unknown Selection, Try Again!\n")


# this function updates the guest controls for the account based on the value passed as the selection and the Account object
def update_guest_controls(selection, user):
    if selection == "1":
        user.incollege_email = not user.incollege_email
    elif selection == "2":
        user.sms = not user.sms
    elif selection == "3":
        user.targeted_ads = not user.targeted_ads
    elif selection == "e":
        user.incollege_email = True
        user.sms = True
        user.targeted_ads = True
    elif selection == "d":
        user.incollege_email = False
        user.sms = False
        user.targeted_ads = False
    else:
        pass


def account_language(user, accounts):
    menu_opt = {"1": "English",
                "2": "Spanish",
                "q": "Return to important links"}
    menu_condition = True
    changed = False
    
    while menu_condition:
        print("\n********* Language *********\n")       
        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])
        selection = input("Select a Option to change to the language or save changes: ")

        if selection == 'q':
            if changed:
                # since user is a reference to the object in the accounts list, we don't have to change the accounts list
                save_accounts_to_csv(accounts)

            menu_condition = False
        elif selection in options:
            if update_account_language(selection, user):
                changed = True
                menu_opt["q"] = "Save changes and return to important links"
        else:
            print("Unknown Selection, Try Again!\n")


def update_account_language(selection, user):
    if selection == "1":
        if user.language == "English":
            print("Language is already set to English\n")
            return False
        else:
            print("Language set to English\n")
            user.language = "English"
            return True
    elif selection == "2":
        if user.language == "Spanish":
            print("Language is already set to Spanish\n")
            return False
        else:
            print("Language set to Spanish\n")
            user.language = "Spanish"
            return True
