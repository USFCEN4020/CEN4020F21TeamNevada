import json
from csv_read_write import *


# API function for all jobs in the system
def output_api_jobs():
    jobs_list = get_jobs_from_csv()

    if len(jobs_list) == 0:
        return jobs_list
    else:
        with open('MyCollege_jobs.txt', 'w', newline='') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for job in jobs_list:
                csv_writer.writerow([job.title])
                csv_writer.writerow([job.description])
                csv_writer.writerow([job.employer])
                csv_writer.writerow([job.location])
                csv_writer.writerow([job.salary])
                csv_writer.writerow(["====="])


# API function for all profiles in the system
def output_api_profile():
    with open('MyCollege_profiles.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        with open("profiles.json", "r") as f:
            contents = json.loads(f.read())

            for profile in contents:
                csv_writer.writerow([profile['title']])
                csv_writer.writerow([profile['major']])
                csv_writer.writerow([profile['university']])
                csv_writer.writerow([profile['about']])
                for job in profile['jobs']:
                    csv_writer.writerow([job['job_name'], job['employer'], job['start_date'], job['end_date'], job['location'], job['description']])
                for edu in profile['education']:
                    csv_writer.writerow([edu['school'], edu['degree'], edu['year']])
                csv_writer.writerow(["====="])


# API function for all users and their membership tier
def output_api_user():
    users_list = get_accounts_from_csv()
    usernames = []
    membership = []

    if len(users_list) == 0:
        return users_list
    else:
        # Gathers all the usernames and their associated tier and places them in the appropriate list
        for user in users_list:
            usernames.append(user.username)
            if user.is_plus:
                membership.append("plus")
            else:
                membership.append("standard")

        with open('MyCollege_users.txt', 'w', newline='') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            i = 0
            while i < len(users_list):
                csv_writer.writerow([usernames[i]])
                csv_writer.writerow([membership[i]])
                i = i + 1


# API function for all training courses taken
def output_api_training():
    # Importing function from learning.py for auxiliary use
    from learning import get_user_courses

    users_list = get_accounts_from_csv()

    if len(users_list) == 0:
        return users_list
    else:
        with open('MyCollege_training.txt', 'w', newline='') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            i = 0
            while i < len(users_list):
                csv_writer.writerow([users_list[i].username])

                # Gets list of all courses the user took and writes them to the file
                user_courses = get_user_courses(users_list[i])
                if len(user_courses) > 0:
                    for course in user_courses:
                        csv_writer.writerow([course])
                csv_writer.writerow(["====="])
                i = i + 1


# API function for all jobs that have been applied for
def output_api_applied_jobs():
    jobs_list = get_jobs_from_csv()

    if len(jobs_list) == 0:
        return jobs_list
    else:
        with open('MyCollege_appliedJobs.txt', 'w', newline='') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            with open("job_application.json", "r") as f:
                contents = json.loads(f.read())

                for job in jobs_list:
                    csv_writer.writerow([job.title])
                    for application in contents:
                        if application['job_title'] == job.title:
                            csv_writer.writerow([application['applicant']])
                            csv_writer.writerow([application['reason']])
                    csv_writer.writerow(["====="])


# API function for all jobs that users have saved for later
def output_api_saved_jobs():
    users_who_saved = set(())

    with open('MyCollege_savedJobs.txt', 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        with open("jobs_saved.json", "r") as f:
            contents = json.loads(f.read())

            # Create set of all users who have saved a job
            for saved_job in contents:
                users_who_saved.add(saved_job["user"])

            for user in users_who_saved:
                csv_writer.writerow([user])
                for saved_job in contents:
                    if saved_job['user'] == user:
                        csv_writer.writerow([saved_job['job_title']])
                csv_writer.writerow(["====="])
