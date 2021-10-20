from csv_read_write import get_accounts_from_csv, save_accounts_to_csv
import json


# Function that allows a user to apply for a job
def apply_job(user, jobs):
    menu_opt = {"1": "Get a Job's Details",
                "2": "Apply For a Job",
                "q": "Return"}

    # Gets the title of all of the listed jobs (potentially none)
    # Used to find the user's selection
    job_list = []
    for x in jobs:
        job_list.append(x.title)

    with open("job_application.json", "r") as f:
        contents = json.loads(f.read())

    # Finds all the jobs that the current user has applied for
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

            # Displays 'APPLIED' next to a job title if it is in applied_list
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

                    # Checks if the user was the one who posted the job
                    for x in jobs:
                        if x.user == user.username and x.title == selection:
                            print("You cannot apply for a job that you have posted!")
                            user_posted = True
                            break

                    if not user_posted:
                        # If the user is creating the first application in 'job_application.json',
                        # We don't need to check anything and allow them to apply
                        if len(contents) == 0:
                            grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
                            start_date = input("Enter the date you that you can start working (mm/dd/yyyy): ")
                            reason = input("Explain why you would be a good fit for this job: ")

                            # Creates application and stores it in 'job_application.json'
                            application = {
                                "job_title": selection,
                                "applicant": user.username,
                                "grad_date": grad_date,
                                "start_date": start_date,
                                "reason": reason
                            }

                            contents.append(application)
                            with open("job_application.json", 'w') as f:
                                json.dump(contents, f)

                            # Increases the number of jobs that the user has applied for
                            updated_accounts = get_accounts_from_csv()
                            for x in updated_accounts:
                                if x.username == user.username:
                                    x.num_applied = x.num_applied + 1
                                    x.num_applied_del = x.num_applied_del + 1

                            save_accounts_to_csv(updated_accounts)

                            break
                        else:
                            # If the user is not creating the first application in 'job_application.json',
                            # Then we check if they have already applied for this job
                            been_applied = False
                            for application in contents:
                                if application['applicant'] == user.username and application['job_title'] == selection:
                                    print("You have already applied for this job!")
                                    been_applied = True
                                    break

                            if not been_applied:
                                grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
                                start_date = input("Enter the date you that you can start working (mm/dd/yyyy): ")
                                reason = input("Explain why you would be a good fit for this job: ")

                                # Creates application and stores it in 'job_application.json'
                                application = {
                                    "job_title": selection,
                                    "applicant": user.username,
                                    "grad_date": grad_date,
                                    "start_date": start_date,
                                    "reason": reason
                                }

                                contents.append(application)
                                with open("job_application.json", 'w') as f:
                                    json.dump(contents, f)

                                # Increases the number of jobs that the user has applied for
                                updated_accounts = get_accounts_from_csv()
                                for x in updated_accounts:
                                    if x == user:
                                        x.num_applied = x.num_applied + 1
                                        x.num_applied_del = x.num_applied_del + 1

                                save_accounts_to_csv(updated_accounts)

                                break

            elif selection == 'q':
                break
            else:
                print("Unknown Selection! Try Again!")
