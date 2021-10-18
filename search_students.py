from profile_class import Profile
import json


# Function to get a user's profile if they have one
def get_profiles_list(user=None):
    profile_obj = Profile()
    if user is not None:
        profile = profile_obj.get_profile_info(user)
    else:
        profile = profile_obj.get_profile_list()
    return profile


# Function to display the list of users who are found by the current user's search criteria
def view_student_list(s_list, user):
    if len(s_list) == 0:
        print("There are no students.")
        return None
    else:
        print("********* View Student Information *********", '\n')
        print("Username \t Firstname \t Lastname \t Major \t University \t Introduction \n")
        for student in s_list:
            print(student["username"], "\t", student["firstname"], "\t", student["lastname"], "\t", student["major"], "\t", student["university"], "\t", student["introduction"], "\n")

        # c_user = user you want to send a request to
        c_user = input("input the username of the student who you want to connect:\n")
        user_count = -1
        for i, student in enumerate(s_list):
            if c_user == student["username"]:
                user_count = i
                break

        if user_count == -1:
            print("Invalid Entry")
        else:
            # content = message to send along with the request
            content = input("input the content to the student you want to connect:\n")

            # Creates the request and adds it to 'friend_connection.json'
            new_connection = {
                "username": user.username,
                "c_user": c_user,
                "content": content
            }
            with open("friend_connection.json", "r") as f:
                connection = json.loads(f.read())
            connection.append(new_connection)
            with open("friend_connection.json", 'w') as f:
                json.dump(connection, f)

            return new_connection


# Function to let user search for users to connect with
def search_students(user, accounts):
    # print(user.get_account_details())
    # print(list(map(lambda a: a.get_account_details(), accounts)))
    if len(accounts) == 0:
        print("There are no accounts.")

    # Must include space when choosing 'last name' option
    option = input("input the option search for students in the system(last name, university, or major):\n")
    if option == "last name":
        s_list = []     # <-- holds results of the search *Does the same for search by 'university' and 'major'
        lastname = input("input the last name:\n")
        for account in accounts:
            if lastname == account.lastname:

                # If found user has a profile, the profile info is included in the search list, else it is not
                # *Same for search by 'university' and 'major'*
                profile = get_profiles_list(account.username)
                if profile is not None:
                    student = {
                        "username": account.username,
                        "firstname": account.firstname,
                        "lastname": account.lastname,
                        "major": profile["major"],
                        "university": profile["university"],
                        "introduction": profile["about"]
                    }
                else:
                    student = {
                        "username": account.username,
                        "firstname": account.firstname,
                        "lastname": account.lastname,
                        "major": None,
                        "university": None,
                        "introduction": None
                    }
                s_list.append(student)
        return view_student_list(s_list, user)
    elif option == "university":
        s_list = []
        university = input("input the university:\n")
        profiles = get_profiles_list()
        for profile in profiles:
            if profile["university"] == university:
                for account in accounts:
                    if account.username == profile["username"]:
                        student = {
                            "username": account.username,
                            "firstname": account.firstname,
                            "lastname": account.lastname,
                            "major": profile["major"],
                            "university": profile["university"],
                            "introduction": profile["about"]
                        }
                        s_list.append(student)
        return view_student_list(s_list, user)
    elif option == "major":
        s_list = []
        major = input("input the major:\n")
        profiles = get_profiles_list()
        for profile in profiles:
            if profile["major"] == major:
                for account in accounts:
                    if account.username == profile["username"]:
                        student = {
                            "username": account.username,
                            "firstname": account.firstname,
                            "lastname": account.lastname,
                            "major": profile["major"],
                            "university": profile["university"],
                            "introduction": profile["about"]
                        }
                        s_list.append(student)
        return view_student_list(s_list, user)
    else:
        print("Invalid Entry")
