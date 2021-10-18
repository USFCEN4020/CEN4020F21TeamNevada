import json


# Function that lets user accept or reject a friend request
def accept_or_reject(user, requesting_user, contents):
    choice = input("Would you like to accept or reject this user (Enter 'a' or 'r'): ")
    if choice == 'a':
        with open("friends_list.json", 'r') as f:
            friends_lists = json.loads(f.read())

        # Finds the user and the requester in 'friends_list.json' and adds each person to the other's friends list
        for f_list in friends_lists:
            if f_list['user'] == user.username:
                f_list['friends'].append(requesting_user.username)

                with open("friends_list.json", 'w') as f:
                    json.dump(friends_lists, f)

            if f_list['user'] == requesting_user.username:
                f_list['friends'].append(user.username)

                with open("friends_list.json", 'w') as f:
                    json.dump(friends_lists, f)

        # Removes the pending request from the list of requests in 'friend_connection.json'
        for connection in contents:
            if connection['username'] == requesting_user.username and connection['c_user'] == user.username:
                contents.remove(connection)

        with open("friend_connection.json", 'w') as f:
            json.dump(contents, f)

    elif choice == 'r':

        # Friends lists are not updated and
        # Removes the pending request from the list of requests in 'friend_connection.json'
        for connection in contents:
            if connection['username'] == requesting_user.username and connection['c_user'] == user.username:
                contents.remove(connection)

        with open("friend_connection.json", 'w') as f:
            json.dump(contents, f)

    else:
        print("Please enter 'a' or 'r'!")


# Function to display the list of pending friend requests to the user and give them options to accept/reject or go back
def pending_requests(user, accounts):
    pending_opt = {"1": "Accept/Reject a Request",
                   "q": "Exit Pending Requests"}

    while True:
        pending_list = []

        # Displays list of pending friend requests
        print("********* Pending Friend Requests ********* \n")

        with open("friend_connection.json", "r") as f:
            contents = json.loads(f.read())

            for connection in contents:
                if connection['c_user'] == user.username:
                    pending_list.append(connection['username'])

        for name in pending_list:
            print(name)

        # Displays list of request options
        print("\n********* PENDING REQUESTS OPTIONS *********")
        options = pending_opt.keys()
        for x in options:
            print(x, ")", pending_opt[x])

        user_choice = input("Choose an option")

        if user_choice == '1':
            if len(pending_list) == 0:
                print("There are no requests to accept or reject!")
            else:
                user_choice = input("Enter the user that you want to accept or reject: ")
                if user_choice not in pending_list:
                    print("User not in list of pending requests!")
                else:
                    for x in accounts:
                        if x.username == user_choice:
                            requesting_user = x
                            accept_or_reject(user, requesting_user, contents)
        elif user_choice == 'q':
            break
        else:
            print("Unknown Selection. Try Again!")


# Function to determine if there is at least 1 pending friend request for the current user
def at_least_1_pending(user):
    count = 0

    with open("friend_connection.json", 'r') as f:
        contents = json.loads(f.read())

    for x in contents:
        if x['c_user'] == user.username:
            count += 1
            break

    return count
