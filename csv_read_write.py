import csv
from account_class import Account
from job_class import Job


# This function reads the account.txt file and returns the accounts or None if no accounts are present
def get_accounts_from_csv():
    accounts = []
    with open('accounts.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            # stores the data from the file to the accounts list
            for row in csv_reader:
                accounts.append(Account(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], int(row[8]), int(row[9]), bool(row[10])))
        except IndexError:  # handles the error if the file is empty
            pass

    return accounts


# This function writes the accounts to the accounts.txt file, overwriting the previous text in the file
def save_accounts_to_csv(accounts):
    # following code updates the database file
    with open('accounts.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # loops through the accounts and writes them to the file
        for account in accounts:
            csv_writer.writerow(account.get_account_details())


# This function reads the jobs.txt file and returns the jobs or None if no jobs are present
def get_jobs_from_csv():
    jobs = []
    with open('jobs.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            # stores the data from the file to the jobs list
            for row in csv_reader:
                jobs.append(Job(row[0],row[1], row[2], row[3], row[4]))
        except IndexError:  # handles the error if the file is empty
            pass

    return jobs


# This function writes the jobs to the jobs.txt file, overwriting the previous text in the file
def save_jobs_to_csv(jobs):
    # following code updates the database file
    with open('jobs.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # loops through the jobs and writes them to the csv file
        for job in jobs:
            csv_writer.writerow(job.get_job_details())
