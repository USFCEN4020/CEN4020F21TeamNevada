from view_message import at_least_1_new_message
import json
from datetime import date, timedelta
from profile_class import Profile
from pending_requests import at_least_1_pending

# function that gets the notifications for a specific user
def get_login_notifications(user):
    notifications = []
    # notifications for friend requests
    if at_least_1_pending(user) > 0:
        notifications.append("You have friend requests waiting for you.")

    # notifications for messages
    if at_least_1_new_message(user) > 0:
        notifications.append("You have messages waiting for you.")

    # notifications for not applying to jobs in the last 7 days
    if not applied_in_7days(user):
        notifications.append("Remember – you're going to want to have a job when you graduate.\n   Make sure that you start to apply for jobs today!")

    # create a profile object to check if the user has a profile created
    # notifications for no profile
    profile_obj = Profile()
    if profile_obj.get_profile_info(user.username) == None:
        notifications.append("Don't forget to create a profile.")
    return notifications
    
def applied_in_7days(user):
    # get the jobs the user has applied for
    with open("job_application.json", "r") as f:
        contents = json.loads(f.read())
    job_dates = []
    for x in contents:
        if x['applicant'] == user.username:
            job_dates.append(date.fromisoformat(x['application_date']))

    # get today's date
    today = date.today()

    # if the user has jobs they have applied for
    # get the number of days between today and the last job application
    if len(job_dates) > 0:
        last_job_date = max(job_dates)
        print(last_job_date.isoformat())
        days_since_last_job = (today - last_job_date).days
        print(days_since_last_job)

        # if the user has not applied for a job in the last 7 days, notify them
        if days_since_last_job > 7:
            return False
        else:
            return True
    else:
        return False