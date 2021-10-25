import json

def send_message_ui(user, accounts): 
    messaging_list = []
    # if the user is a standard user, they can select from their friends
    if not user.is_plus:
        # read in the friends list file
        with open("friends_list.json", 'r') as f:
            contents = json.loads(f.read())

        # get the current users friends
        for x in contents:
            if x['user'] == user.username:
                for y in x['friends']:
                    messaging_list.append(y)
    else:
        # if the user is a plus user, they can select from all users
        for x in accounts:
            # add the user to the messaging list if they are not the current user
            if x.username != user.username:
                messaging_list.append(x.username)

    # while the user input is valid
    recipient = ""
    while True:
    # print out the users to message
        print("\n********* Send a message *********\n")
        for x in messaging_list:
            print(x)
        recipient = input("\nEnter the user you would like to message or\nenter quit to go back: ")

        # if the user is not in the messaging list, print an error message
        if recipient not in messaging_list:
            # if the user enters quit, return to the main menu
            if recipient == "quit":
                return
            else:
                print("\nYou are not able to message that user.")
        else:
            # if the user is in the messaging list, break out of the loop
            break
    
    # have the user enter the message they would like to send
    print("\nEnter the message you would like to send to", recipient)
    message = input(": ")

    # confirm the message
    print("\nYour message to", recipient, "says\n", message)
    confirmation = input("\nWould you like to send this message? (y/n): ")

    # if the user confirms the message, send it
    if confirmation == "y":
        send_message(user, recipient, message)
        print("\nMessage sent.")
        return
    else:
        # return back to the messaging menu
        return


def send_message(user, recipient, message):
    pass