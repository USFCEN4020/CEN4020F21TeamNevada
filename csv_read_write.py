import csv
from account_class import Account


# This function reads the csv file and returns the accounts or None if no accounts are present
def get_accounts_from_csv():
    accounts = []
    with open('accounts.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            # stores the data from the csv file to the accounts list
            for row in csv_reader:
                accounts.append(Account(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        except IndexError:  # handles the error if the csv file is empty
            pass

    return accounts


# This function writes the accounts to the csv file, overwriting the previous text in the file
def save_accounts_to_csv(accounts):
    # following code updates the database file
    with open('accounts.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # loops through the accounts and writes them to the csv file
        for account in accounts:
            csv_writer.writerow(account.get_account_details())

