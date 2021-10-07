import string


def profile_creation():
    print("********* Profile Creation *********")
    print("Enter your title: ")
    title_ = input()

    print("Enter your major: ")
    major_ = input()
    capital_major = string.capwords(major_)  # Code so input is converted to and upper case and the rest lowercase

    print("Enter University name: ")
    university_ = input()
    capital_university = string.capwords(
        university_)  # Code so input is converted to and upper case and the rest lowercase

    print("Enter information about you: ")
    about_ = input()

    print("Enter experience (y/n)")
    choice = input()
    if choice == "y":
        jobs = []
        for i in range(3):
            print("Enter job title: ")
            title_ = input()
            print("Enter Employer: ")
            employer_ = input()
            print("Enter start date: ")
            start_date = input()
            print("Enter end date: ")
            end_date = input()
            print("Enter location: ")
            location_ = input()
            print("Enter job description: ")
            description_ = input()
            print("Would you like to enter another job? (y/n)")
            data = input()
            if str.lower(data) == "y":
                print("Enter another job")
                continue
            elif str.lower(data) == "n":
                break
            else:
                print("Invalid entry.\n")
            jobs.append(data)
    elif choice == "n":
        print("\n")
    else:
        print("Invalid Entry")

    print("********* Provide Education information *********")
    print("Enter school name")
    attended_school = input()
    print("Enter degree")
    degree_ = input()
    print("Enter Years attended: ")
    years_attended = input()

"""
    print("\n",title_, "\n", capital_major,"\n", capital_university, "\n", about_ ) #Tentative for Dogni
    print("\n",attended_school,"\n", degree_,"\n", years_attended) #Tentative for Dogni
"""

