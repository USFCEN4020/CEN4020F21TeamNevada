import os.path
from account_class import Account
from csv_read_write import save_accounts_to_csv


def input_accounts(accounts):
    # check if the file exists
    if not os.path.isfile("studentAccouts.txt"):
        return accounts
    else:
        with open("studentAccouts.txt", "r") as f:
            context = f.readlines()
            if len(context) == 0:
                return accounts
            else:
                index = 0
                while index < len(context):
                    # username, first name and last name are in the same line split by ","
                    user_info = context[index].strip().split(",")
                    pwd = context[index+1].strip()
                    is_exist = False
                    # if the username exists, then save the information in accounts.txt
                    for account in accounts:
                        if account.username == user_info[0]:
                            is_exist = True
                    if is_exist:
                        index += 3
                        continue
                    else:
                        # save the information into accounts.txt
                        create_account_ = Account(user_info[0], pwd, user_info[1], user_info[2])
                        accounts.append(create_account_)
                        save_accounts_to_csv(accounts)
                        index += 3
                    # if the number of users large than 10, return the accounts
                    if len(accounts) >= 10:
                        return accounts
                return accounts
