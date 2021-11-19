from job_class import *
from csv_read_write import save_jobs_to_csv, get_accounts_from_csv
from output_api import output_api_jobs
import json


# Function to create job posting
def create_job(user, jobs):
    # checks for 10 stored jobs listings
    line_count = len(jobs)
    if line_count >= 10:
        print("The listing limit has been reached. Only 10 jobs are permitted to be posted at a time.")
        return

    title_ = input("Job Title: ")
    description_ = input("Job Description: ")
    employer_ = input("Job Employer: ")
    salary_ = input("Job Salary: ")
    location_ = input("Job's Location: ")

    # following code creates a job object to "post" a Job
    created_job_ = Job(user.username, title_, description_, employer_, salary_, location_)
    jobs.append(created_job_)

    # create a notification for the new job in global_notifications.json
    new_job_notif(user, title_)

    # Saves jobs
    save_jobs_to_csv(jobs)

    # API call for all jobs listed in InCollege
    output_api_jobs()

    print("Your Job was posted successfully!\n")

    return jobs


# Notifies the user when a job has been posted
def new_job_notif(user, job_name):
    # adds a notification in global notifications for the current accounts that a new job was created
    # get the contents of the global notifications json
    with open("global_notifications.json", "r") as f:
        contents = json.loads(f.read())

    # get all of the accounts from csv
    accounts = get_accounts_from_csv()

    # loop through all of the accounts
    for account in accounts:
        if not account.username == user.username:
            contents.append({
                "username": account.username,
                "notification": ("A new job " + job_name + " has been posted.")
            })

    # write the contents to the global notifications json
    with open("global_notifications.json", "w") as f:
        json.dump(contents, f)