import os.path
from job_class import Job
from csv_read_write import save_jobs_to_csv


def input_jobs(jobs):
    # check if the file exists
    if not os.path.isfile("newJobs.txt"):
        return jobs
    else:
        with open("newJobs.txt", "r") as f:
            context = f.readlines()
            if len(context) == 0:
                return jobs
            else:
                index = 0
                # d_list uses to save the index of "&&&"
                d_list = []
                # i_list uses to save the index of "====="
                i_list = [-1]
                while index < len(context):
                    info = context[index].strip()
                    if info == "&&&":
                        d_list.append(index)
                    if info == "=====":
                        i_list.append(index)
                    index += 1
                for i in range(len(d_list)):
                    title_ = context[i_list[i]+1].strip()
                    description_ = context[i_list[i]+2:d_list[i]]
                    line_ = ""
                    for line in description_:
                        line = line.strip()
                        line_ += line
                    user_ = context[d_list[i]+1].strip()
                    employer_ = context[d_list[i]+2].strip()
                    location_ = context[d_list[i]+3].strip()
                    salary_ = context[d_list[i]+4].strip()
                    # check if the title of job is existed
                    is_exist = False
                    for job in jobs:
                        if job.title == title_:
                            is_exist = True
                    if is_exist:
                        continue
                    else:
                        # save the job information into jobs.txt
                        created_job_ = Job(user_, title_, line_, employer_, salary_, location_)
                        jobs.append(created_job_)
                        save_jobs_to_csv(jobs)
                    if len(jobs) >= 10:
                        return jobs
                return jobs