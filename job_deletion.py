from csv_read_write import get_accounts_from_csv, save_accounts_to_csv
from output_api import output_api_jobs
import json


# Function that allows a user to delete a job that they have posted
def delete_job(user, jobs):
    menu_opt = {"1": "Select a Job to Delete",
                "q": "Return"}

    while True:
        # Finds all of the jobs that the current user has posted (potentially none)
        user_posted = []
        for x in jobs:
            if x.user == user.username:
                user_posted.append(x.title)

        if len(user_posted) == 0:
            print("\n ********* List of Jobs You Have Posted ********* \n")

            print("\n You have no posted jobs! \n")
            break
        else:
            print("\n ********* List of Jobs You Have Posted ********* \n")

            for x in user_posted:
                print(x)
            print("\n")

            options = menu_opt.keys()
            for x in options:
                print(x, ")", menu_opt[x])

            selection = input("Select an Option: ")

            if selection == '1':
                selection = input("Select the job you want to delete: ")

                if selection in user_posted:
                    for x in jobs:
                        if x.user == user.username and x.title == selection:
                            # Temporary variables for the job info
                            user_ = x.user
                            title_ = x.title
                            description_ = x.description
                            employer_ = x.employer
                            salary_ = x.salary
                            location_ = x.location

                            # Removes job from the job list
                            jobs.remove(x)

                            # Following code removes the job from the jobs.txt file
                            contents = open("jobs.txt", "r")
                            lines = contents.readlines()
                            contents.close()

                            new_contents = open("jobs.txt", "w")
                            for line in lines:
                                if line.strip(
                                        "\n") != user_ + "," + title_ + "," + description_ + "," + employer_ + "," + salary_ + "," + location_:
                                    new_contents.write(line)

                            new_contents.close()

                            # Following code removes all applications for the job from 'job_application.json'
                            # And decreases the number of jobs that the associated applicants have applied for
                            with open("job_application.json", "r") as f:
                                contents = json.loads(f.read())

                            updated_accounts = get_accounts_from_csv()

                            for application in contents:
                                if application['job_title'] == selection:
                                    for y in updated_accounts:
                                        if y.username == application['applicant']:
                                            # create global notification for applicant of deleted jobs
                                            job_deleted_notif(y, title_)

                                            if y.num_applied_del > 0:
                                                y.num_applied_del = y.num_applied_del - 1

                                    contents.remove(application)

                            with open("job_application.json", 'w') as f:
                                json.dump(contents, f)

                            save_accounts_to_csv(updated_accounts)

                            # API call for all jobs listed in InCollege
                            output_api_jobs()

                            print("\n This job will no longer be posted.")

                            break
                else:
                    print("That is not a job you have posted!")
            elif selection == 'q':
                break
            else:
                print("Unknown Selection! Try Again!")


# Function to determine if any jobs the user applied for have been deleted
def user_job_deleted(user):
    print()
    if user.num_applied > user.num_applied_del:
        updated_accounts = get_accounts_from_csv()

        for x in updated_accounts:
            if x.username == user.username:
                x.num_applied = x.num_applied_del  # Updates to the correct number of jobs applied for
                break

        save_accounts_to_csv(updated_accounts)

        return True
    else:
        return False


# Notifies the user that a job that they applied for was deleted
def job_deleted_notif(user, job_name):
    # adds a notification in global notifications for the current accounts that a new account was created

    # get the contents of the global notifications json
    with open("global_notifications.json", "r") as f:
        contents = json.loads(f.read())

    contents.append({
        "username": user.username,
        "notification": ("The job "+job_name+" you applied for was deleted.")
    })

    # write the contents to the global notifications json
    with open("global_notifications.json", "w") as f:
        json.dump(contents, f)
