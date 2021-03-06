import json


# function to determine if there is a new message for a user
def at_least_1_new_message(user):
    count = 0

    with open("new_messages.json", 'r') as f:
        messages = json.loads(f.read())

    for x in messages:
        if x["recipient"] == user.username:
            count += 1
            break

    return count

# gets the user's new messages
def get_new_messages(user):
    messages = []
    # get the user's new messages
    with open("new_messages.json", 'r') as f:
        contents = json.loads(f.read())

    for x in contents:
        if x["recipient"] == user.username:
            messages.append(x)

    return messages

# gets the user's saved messages
def get_saved_messages(user):
    messages = []
    # get the user's saved messages
    with open("saved_messages.json", 'r') as f:
        contents = json.loads(f.read())

    for x in contents:
        if x["recipient"] == user.username:
            messages.append(x)

    return messages

def view_messages_ui(user, accounts):
    while True:
        # get the user's new messages
        new_messages = get_new_messages(user)

        # get the user's saved messages
        saved_messages = get_saved_messages(user)

        # if the user has either new or saved messages, print the view messages options
        # otherwise, print you have no messages
        if len(new_messages) > 0 or len(saved_messages) > 0:
            print("\n ********* View Messages Options ********* \n")

            # keep track of the number of options
            count = 1

            # if the user has new messages, print the new messages option
            #if len(new_messages) > 0:
            print(str(count) + ") View New Messages")
            count += 1

            # if the user has saved messages, print the saved messages option
            #if len(saved_messages) > 0:
            print(str(count) + ") View Saved Messages")
            #    count += 1

            # print the quit option
            print("q) Quit")

            view_messages_selection = input("Select an Option: ")

            # if the user selected to view new messages, go to the view new messages function
            if view_messages_selection == "1":
                view_new_messages(user, new_messages)
            elif view_messages_selection == "2":
                view_saved_messages(user, saved_messages)
            elif view_messages_selection == "q":
                return
            else:
                print("Unknown Selection, Try Again!")
        else:
            print("\n ** You have no messages, returning to messages menu **\n")
            return

def view_new_messages(user, new_messages):
    while True:
        # if new messages length if greater than 0, print the new messages options
        if len(new_messages) > 0:
            # print the new messages
            print("\n ********* New Messages ********* \n")
            for num, message in enumerate(new_messages):
                print("New message #"+str(num+1)+": ")
                print("From: " + message["sender"] + "\n")
                print("Message: " + message["message"] + "\n")
                print("\n")

            # print the view messages options
            message_option = input("Enter a message number to save the message\nor q to quit and delete unsaved new messages:")

            # try to convert the message option to an integer
            try:
                message_option = int(message_option)

                # if the integer is in the range of the new messages, save the message
                if message_option <= len(new_messages):
                    # save the message
                    save_message(user, new_messages[message_option-1])

                    # remove the message from the new messages list
                    new_messages.remove(new_messages[message_option-1])
                else:
                    print("Unknown Selection, Try Again!")
            except ValueError:
                # if message option is q, quit and delete unsaved new messages
                if message_option == "q":
                    print("\n ** Deleting unsaved new messages **\n")
                    delete_new_messages(user)
                    return
                else:
                    print("Unknown Selection, Try Again!")
        else:
            print("\n ** You have no new messages, returning to messages menu **\n")
            delete_new_messages(user)
            return

def view_saved_messages(user, saved_messages):

    while True:
        # if new messages length if greater than 0, print the new messages options
        # print(len(saved_messages))
        if len(saved_messages) > 0:
            # print the new messages
            print("\n ********* Saved Messages ********* \n")
            for num, message in enumerate(saved_messages):
                print("New message #"+str(num+1)+": ")
                print("From: " + message["sender"] + "\n")
                print("Message: " + message["message"] + "\n")
                print("\n")

            # print the view messages options
            message_option = input("Enter a message number to delete\n else q to quit")

            # try to convert the message option to an integer
            try:
                message_option = int(message_option)

                # if the integer is in the range of the new messages, save the message
                if message_option <= len(saved_messages):
                    # remove the message from the saved messages list
                    saved_messages.remove(saved_messages[message_option-1])
                    delete_saved_message(user)
                else:
                    print("Unknown Selection, Try Again!")
            except ValueError:
                # if message option is q, quit and delete unsaved new messages
                if message_option == "q":
                    return
                else:
                    print("Unknown Selection, Try Again!")
        else:
            print("\n ** You have no saved messages **\n")
            return

# this function deletes all new messages for a user
def delete_new_messages(user):

    with open("new_messages.json", "r") as fs:
        new_messages = json.loads(fs.read())

    new_messages = [i for i in new_messages if not (i['recipient'] == user.username)]

    with open("new_messages.json", "w") as fs:
        json.dump(new_messages, fs)

# this function deletes one single message for a user
def delete_saved_message(user):

    with open("saved_messages.json", "r") as fs:
        saved_messages = json.loads(fs.read())

    # JSON File popping
    for i in range(len(saved_messages)):
        if saved_messages[i]['recipient'] == user.username:
            saved_messages.pop(i)
            break

    with open("saved_messages.json", "w") as fs:
        json.dump(saved_messages, fs)

# this function saves a message for a user by adding it to the saved messages file
def save_message(user, message):

    with open("saved_messages.json", "r") as f:
        messageInfo = json.loads(f.read())

    savedMessage = {
                "recipient": user.username,
                "sender": message["sender"],
                "message": message["message"]
            }

    messageInfo.append(savedMessage)
    with open("saved_messages.json", "w") as f:
        json.dump(messageInfo, f)