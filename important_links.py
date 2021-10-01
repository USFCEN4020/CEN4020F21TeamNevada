def important_links_groups():
    # Prints the InCollege important Links menu
    menu_opt = {"1": "Copyright Notice",
                "2": "About",
                "3": "Accessibility",
                "4": "User Agreement",
                "5": "Privacy Policy",
                "6": "Cookie Policy",
                "7": "Copyright Policy",
                "8": "Brand Policy",
                "q": "Return to home screen"}
    while True:
        print("\n********* Important Link Groups ********* \n")
        options = menu_opt.keys()
        for x in options:
            print(x, ")", menu_opt[x])

        selection = input("Select an Option: ")
        if selection == '1':
            print("********* Copyright Notice *********")
        elif selection == '2':
            print("********* About *********")
        elif selection == '3':
            print("********* Accessibility *********")
        elif selection == '4':
            print("********* User Agreement *********")
        elif selection == '5':
            print("********* Privacy Policy *********")
        elif selection == '6':
            print("********* Cookie Policy  *********")
        elif selection == '7':
            print("********* Copyright Policy *********")
        elif selection == '8':
            print("********* Brand Policy *********")
        elif selection == 'q':
            print("\n")
            break
        else:
            print("Invalid Selection, Try Again!")
