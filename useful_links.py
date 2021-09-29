def useful_links_groups():
    # following code prints the useful links menu
    menu_opt = {"1": "General",
                "2": "Browse InCollege",
                "3": "Business Solutions",
                "4": "Directories",
                "q": "Return to home screen"}

    while True:
        print("\n ********* Useful Links Groups ********* \n")
        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")
        if selection == '1':
            # if the users selected signup from the general links, we need to return back to the login screen
            # to direct them to the create new account screen
            signup_selected = general_links()
            if signup_selected:
                return True
        elif selection == '2':
            print("Under construction")
        elif selection == '3':
            print("Under construction")
        elif selection == '4':
            print("Under construction")
        elif selection == 'q':
            print("\n")
            break
        else:
            print("Unknown Selection, Try Again!")


def general_links():
    # prints the options for the general links
    menu_opt = {"1": "Sign Up",
                "2": "Help Center",
                "3": "About",
                "4": "Press",
                "5": "Blog",
                "6": "Careers",
                "7": "Developers",
                "q": "Return to useful links screen"}

    while True:
        print("\n ********* General Links ********* \n")
        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")

        if selection == '1':
            # if the user selected sign up, we need to direct the program flow back to the
            # login screen so they can be directed to the create account screen
            return True
        elif selection == '2':
            print("We're here to help")
        elif selection == '3':
            print("In College: Welcome to In College, the world's largest college student")
            print("network with many users in many countries and territories worldwide.")
        elif selection == '4':
            print("In College Pressroom: Stay on top of the latest news, updates, and reports.")
        elif selection == '5':
            print("Under construction")
        elif selection == '6':
            print("Under construction")
        elif selection == '7':
            print("Under construction")
        elif selection == 'q':
            return False
        else:
            print("Unknown Selection, Try Again!")
