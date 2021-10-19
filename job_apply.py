from job_class import *
from csv_read_write import get_jobs_from_csv
import json


def apply_job(user, jobs):
    menu_opt = {"1": "Get a Job's Details",
                "2": "Apply For a Job",
                "q": "Return"}

    job_list = []
    for x in jobs:
        job_list.append(x.title)

    with open("job_application.json", "r") as f:
        contents = json.loads(f.read())

    applied_list = []
    for x in contents:
        if x['applicant'] == user.username:
            applied_list.append(x['job_title'])

    while True:
        if len(jobs) == 0:
            print("\n ********* Available Jobs ********* \n")

            print("\n There are no available jobs! \n")
            break
        else:
            print("\n ********* Available Jobs ********* \n")

            for x in jobs:
                if x.title in applied_list:
                    print(x.title, "APPLIED")
                else:
                    print(x.title)
            print("\n")

            options = menu_opt.keys()
            for x in options:
                print(x, ")", menu_opt[x])

            selection = input("Select an Option: ")

            if selection == '1':
                pass
                # Tentative for "Display Job Information" story
            elif selection == '2':
                selection = input("Select a job to apply for: ")

                if selection not in job_list:
                    print("That job is not available!")
                elif selection in job_list:
                    user_posted = False
                    print("job in")
                    for x in jobs:
                        if x.user == user.username and x.title == selection:
                            print("You cannot apply for a job that you have posted!")
                            user_posted = True
                            break

                    if not user_posted:
                        print("before")
                        if len(contents) == 0:
                            print("after")
                            print("job not applied")
                            grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
                            start_date = input("Enter the date you that you can start working (mm/dd/yyyy): ")
                            # reason

                            application = {
                                "job_title": selection,
                                "applicant": user.username,
                                "grad_date": grad_date,
                                "start_date": start_date
                            }

                            contents.append(application)
                            with open("job_application.json", 'w') as f:
                                json.dump(contents, f)

                            user.num_applied = user.num_applied + 1

                            break
                        else:
                            been_applied = False
                            for application in contents:
                                if application['applicant'] == user.username and application['job_title'] == selection:
                                    print("You have already applied for this job!")
                                    been_applied = True
                                    break

                            if not been_applied:
                                print("job not applied")
                                grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
                                start_date = input("Enter the date you that you can start working (mm/dd/yyyy): ")
                                # reason

                                application = {
                                    "job_title": selection,
                                    "applicant": user.username,
                                    "grad_date": grad_date,
                                    "start_date": start_date
                                }

                                contents.append(application)
                                with open("job_application.json", 'w') as f:
                                    json.dump(contents, f)

                                user.num_applied = user.num_applied + 1

                                break

            elif selection == 'q':
                break
            else:
                print("Unknown Selection! Try Again!")

