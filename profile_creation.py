import string

"""
TO DO: (Yinet)
1. Finish up Experience section 
2. Make paragraph look certain way
"""

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

    """print("Enter job experience (y/n)")
    choice = ' '"""

    print("********* Provide Education information *********")
    print("Enter school name")
    attended_school = input()
    print("Enter degree")
    degree_ = input()
    print("Enter Years attended: ")
    years_attended = input()

    print("\n",title_, "\n", capital_major,"\n", capital_university, "\n", about_ )
""" if choice == 'y':
        job_experience()
    elif choice == 'n':
        print("\n")
    # break
    else:
        print("\nUnknown Selection. Try Again!\n")
"""
    print("\n",attended_school,"\n", degree_,"\n", years_attended)
"""
def job_experience():
    print("You may enter up to 3 jobs. How many past jobs would you like to enter:")
    job_num = input()
    if (1 <= job_num) or (job_num <= 3):
        for i in range(job_num):
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
            print(title_, employer_, start_date, end_date, location_, description_)
        else:
            print("Please, enter up to 3 jobs: ")
        # break
"""