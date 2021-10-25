import json

# function to determine if there is a new message
def at_least_1_new_message(user):
    count = 0

    with open("new_messages.json", 'r') as f:
        messages = json.loads(f.read())

    for x in messages:
        if x["recipient"] == user.username:
            count += 1
            break

    return count