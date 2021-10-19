from job_class import *
from csv_read_write import save_jobs_to_csv
import json


def delete_job(user, jobs, accounts):
    menu_opt = {"1": "Select a Job to Delete",
                "q": "Return"}

    while True:
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

                            # Removes job from the job list
                            jobs.remove(x)

                            # Following code removes the job from the jobs.txt file
                            contents = open("jobs.txt", "r")
                            lines = contents.readlines()
                            contents.close()

                            new_contents = open("jobs.txt", "w")
                            for line in lines:
                                if line.strip("\n") != user_ + "," + title_ + "," + description_ + "," + employer_ + "," + salary_:
                                    new_contents.write(line)

                            new_contents.close()

                            with open("job_application.json", "r") as f:
                                contents = json.loads(f.read())

                            for application in contents:
                                if application['job_title'] == selection:
                                    for y in accounts:
                                        if y.username == application['applicant']:
                                            if y.num_applied > 0:
                                                y.num_applied = y.num_applied - 1

                                    contents.remove(application)

                            with open("job_application.json", 'w') as f:
                                json.dump(contents, f)

                            print("\n This job will no longer be posted.")

                            break
                else:
                    print("That is not a job you have posted!")
            elif selection == 'q':
                break
            else:
                print("Unknown Selection! Try Again!")
