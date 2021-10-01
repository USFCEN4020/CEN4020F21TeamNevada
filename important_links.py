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
        elif selection == 'q':
            print("\n")
            break
        else:
            print("Invalid Selection, Try Again!")
