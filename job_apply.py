from job_class import *
from csv_read_write import get_jobs_from_csv
import json


def apply_job(user, jobs):
    menu_opt = {"1": "Get a Job's Details",
                "2": "Apply For a Job",
                "3": "Save a Job for Later",
                "4": "View saved Jobs",
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
    
    with open("jobs_saved.json", "r") as fs:
        saved_jobs = json.loads(fs.read())

    saved_list = []
    for x in saved_jobs:
        if x['user'] == user.username:
            saved_list.append(x['job_title'])

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

            # Display Job Information selection
            if selection == '1':
                selection = input("Select to view Details: ")
                if selection not in job_list:
                    print("That job does not exist!")
                elif selection in job_list:
                    for x in jobs:
                        if selection == x.title:
                            print("\n *********",selection,"********* \n")
                            print("Description:",x.description)
                            print("Employeer: ",x.employer)
                            print("Location: N/A")
                            print("Salary: ",x.salary,"\n")
                            break       
            # Apply for a  selection    
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
            # Save for later Job Selection
            elif selection == '3':
                selection = input("Select a job to save: ")
                if selection not in job_list:
                    print("That job does not exist!")
                elif selection in job_list and selection not in saved_list:
                    job = {
                                "job_title": selection,
                                "user": user.username,
                                }
                    saved_jobs.append(job)
                    with open("jobs_saved.json", "w") as fs:
                        json.dump(saved_jobs, fs)
                    break
                else:
                    print("You have already saved this job!")
                    break
            # View all saved Jobs
            elif selection == '4':
                menu_sav = {"1":"Unsave Job",
                            "q":"return"}

                print("\n ********* Saved Jobs ********* \n")
                for job in saved_list:
                    if job in applied_list:
                        print(job, "APPLIED")
                    else:
                        print(job)
                
                options = menu_sav.keys()
                for x in options:
                    print(x, ")", menu_sav[x])

                selection = input("Select an Option: ")

                if selection == '1':
                    selection = input("Unsave job: ")
                    if selection not in saved_list:
                        print("Job is not already saved!")
                    else:
                        # JSON File popping
                        for i in range(len(saved_jobs)):
                            if saved_jobs[i]['job_title'] == selection and saved_jobs[i]['user'] == user.username:
                                saved_jobs.pop(i)
                                break

                        with open("jobs_saved.json", "w") as fs:
                            json.dump(saved_jobs, fs)

                        print("Job", selection, "removed from saved list.")
                        break
                elif selection == 'q':
                    break
                else:
                    print("Unknown Selection! Try Again!")
                
            #  Quit
            elif selection == 'q':
                break
            else:
                print("Unknown Selection! Try Again!")

