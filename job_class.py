class Job:
    # Job class constructor
    def __init__(self, user, title, description, employer, salary, location="none"):
        self.user = user
        self.title = title
        self.description = description
        self.employer = employer
        self.salary = salary
        self.location = location

    # Returns a list of the Jobs class object properties to be used for writing to the csv file
    def get_job_details(self):
        return [self.user, self.title, self.description, self.employer, self.salary, self.location]
