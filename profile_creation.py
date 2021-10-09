import string
from profile_class import Profile

#Code to view user's profile
def view_profile():
    user = input("input the user you want to view:\n")
    profile_obj = Profile()
    profile = profile_obj.get_profile_info(user)
    if profile is None:
        print("the user does not exist!")
        return
    print()
    print_profile(profile)

#Code to print the user profile
def print_profile(pro_info):
    print("********* View Profile Information *********", '\n')
    print("Name: ", pro_info['username'], "\n")
    print("Title: ", pro_info['title'], '\n')
    print("Major: ", pro_info['major'], '\n')
    print("University: ", pro_info['university'], '\n')
    print("Information: ", pro_info['about'], '\n')
    print("Education Information: ", '\n')
    jobs = pro_info["jobs"]
    if jobs is not None:
        print("Job experience: \n")
        for job in jobs:
            print("\t job name: ", job['job_name'], "\n\t employer: ",
                  job['employer'], "\n\t start date: ", job['start_date'], "\n\t end date: ", job['end_date'], "\n\t location: ", job['location'], "\n\t description: ", job['description'], "\n")
    education = pro_info['education']
    if education is not None:
        print("Education experience: \n")
        for e in education:
            print("\t school: ", e["school"], "\n\t degree: ", e['degree'], "\n\t year: ", e['year'], "\n")

#Code will create user profile
def profile_creation(user):
    old_profile = Profile(user.username)
    old_profile_info = old_profile.get_profile_info(user.username)
    old_state = False
    if old_profile_info is not None:
        old_state = True
    print("********* Profile Creation *********")
    if old_state and (old_profile_info['title'] is not None):
        print("Current title is ", old_profile_info['title'])
    data = input("Enter your title: \n").strip()
    if data == '':
        title_ = old_profile_info['title']
    else:
        title_ = data

    if old_state and (old_profile_info['major'] is not None):
        print("Current major is ", old_profile_info['major'])
    major = input("Enter your major: \n").strip()
    if major == '':
        major_ = old_profile_info['major']
    else:
        major_ = major
    # Code so input is converted to an upper case and the rest lowercase
    capital_major = string.capwords(major_)

    if old_state and (old_profile_info['university'] is not None):
        print("Current university is ", old_profile_info['university'])
    university = input("Enter University name: \n").strip()
    if university == "":
        university_ = old_profile_info['university']
    else:
        university_ = university
    capital_university = string.capwords(
        university_)  # Code so input is converted to an upper case and the rest lowercase

    if old_state and (old_profile_info['about'] is not None):
        print("Current information about you is ", old_profile_info['about'])
    about = input("Enter information about you: \n").strip()
    if about == '':
        about_ = old_profile_info['about']
    else:
        about_ = about

    #Code will ask user for experience
    print("Enter experience (y/n)")
    choice = input()
    jobs = []
    if choice == "y":
        while True:
            print("Enter job title: ")
            job_title_ = input()
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
            jobs.append({
                "job_name": job_title_,
                "employer": employer_,
                "start_date": start_date,
                "end_date": end_date,
                "location": location_,
                "description": description_
            })
            print("Would you like to enter another job? (y/n)")
            data = input()
            if str.lower(data) == "y":
                print("Enter another job")
                continue
            elif str.lower(data) == "n":
                break
            else:
                print("Invalid entry.\n")
    elif choice == "n":
        print("\n")
    else:
        print("Invalid Entry")

    print("jobs", jobs)

    #Code will ask user for Education
    print("********* Provide Education information *********")
    education = []
    print("Enter school information:", '\n')
    while True:
        print("Enter school name:")
        attended_school = input()
        print("Enter degree:")
        degree_ = input()
        print("Enter Years attended: ")
        years_attended = input()
        education.append({
            "school": attended_school,
            "degree": degree_,
            "year": years_attended
        })
        print("Would you like to enter another education information? (y/n)")
        data = input()
        if str.lower(data) == "y":
            print("Enter another education information.")
            continue
        elif str.lower(data) == "n":
            break
        else:
            print("Invalid entry.\n")

    new_profile = Profile(user.username, title_, capital_major,
                          capital_university, about_, jobs, education)
    new_profile.write_profile_info()
    pro_info = new_profile.get_profile_info(user.username)
    print_profile(pro_info)

