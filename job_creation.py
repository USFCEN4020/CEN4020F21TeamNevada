from job_class import *
from csv_read_write import save_jobs_to_csv


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

    # following code creates a job object to "post" a Job
    created_job_ = Job(user.username, title_, description_, employer_, salary_)
    jobs.append(created_job_)

    save_jobs_to_csv(jobs)

    print("Your Job was posted successfully!\n")

    return jobs
