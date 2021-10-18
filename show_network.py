from profile_class import Profile
from profile_creation import print_profile
import json


# Function to display the user's list of friends and give them options to delete friends + view profiles
def show_network(user):
    friend_opt = {"1": "Delete a friend",
                  "2": "View a Friend's Profile",
                  "q": "Exit Your Network"}

    # List of users who have created profiles
    user_profiles = []

    # List of user's current friends
    current_friends = []

    while True:
        with open("friends_list.json", 'r') as f:
            contents = json.loads(f.read())

        # Gets all user's that have created profiles
        with open("profiles.json", 'r') as f:
            profile_contents = json.loads(f.read())
            for x in profile_contents:
                user_profiles.append(x['username'])

        # Gets the user's current friends list
        for x in contents:
            if x['user'] == user.username:
                for y in x['friends']:
                    current_friends.append(y)

        # Displays user's list of friends
        print("\n ********* Your Friends List ********* \n")
        for x in contents:
            if x['user'] == user.username:
                for y in x['friends']:      # Loop determines each friend has created a profile or not
                    if y in user_profiles:  # (meaning friend is in 'user_profiles' list) and displays 'PROFILE' option
                        print(y, "PROFILE")
                    else:
                        print(y)

        # Displays list of friend options
        print("\n********* FRIEND OPTIONS *********")
        options = friend_opt.keys()
        for x in options:
            print(x, ")", friend_opt[x])

        choice = input("Select an Option")
        if choice == '1':
            if len(current_friends) == 0:
                print("Your friend's list is empty!")
            else:
                condition = True
                while condition:
                    choice = input("Which friend would you like to delete?")
                    for x in contents:
                        if x['user'] == user.username:
                            if choice in x['friends']:       # If statement makes sure friend is in user's friends list
                                x['friends'].remove(choice)  # before deletion
                            else:
                                print("This user is not in your friends list!")
                                break

                        if x['user'] == choice:              # Deletes user from the ex-friend's list
                            x['friends'].remove(user.username)
                            condition = False

                    if not condition:
                        break

                # Update contents of 'friends_list.json'
                with open("friends_list.json", 'w') as f:
                    json.dump(contents, f)

        elif choice == '2':
            if len(current_friends) == 0:
                print("Your friend's list is empty!")
            else:
                while True:
                    print("NOTE: You can only view a friends profile if the 'PROFILE' option is displayed by their name")
                    choice = input("Which friend's profile would you like to view? (Enter 'q' to go back)")

                    if choice == 'q':
                        break
                    elif choice not in current_friends:
                        print("This user is not in your friends list!")
                    elif choice not in user_profiles:
                        print("This user does not have a profile!")
                    else:
                        profile_obj = Profile()
                        profile = profile_obj.get_profile_info(choice)
                        print_profile(profile)
                        break
        elif choice == 'q':
            break
        else:
            print("Unknown Selection, Try Again!")
