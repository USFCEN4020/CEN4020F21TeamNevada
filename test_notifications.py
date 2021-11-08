import unittest
import mock
from main import *
from job_class import Job
from account_class import Account
from job_creation import new_job_notif
from send_message import *
from view_message import *
from profile_creation import *
from account_creation import new_user_notif
from job_apply import *
from job_deletion import *
from notifications import *


class TestCases(unittest.TestCase):
    
    # Tests the notifications for jobs you currently have applied for.
    def test_notification_currently_applied(self):
        test_acc1 = Account("john", "John123!", "John", "Doe")
        test_accounts = []
        test_jobs = []

        application1 = {
            "job_title": 'sw engineer',
            "applicant": test_acc1.username,
            "grad_date": '12/11/2021',
            "start_date": '12/12/2021',
            "reason": 'I am a hard worker.',
            "application_date": date.today().isoformat()
        }

        # Adds the test applications to job_application.json
        with open("job_application.json", 'r') as f:
            contents = json.loads(f.read())

        contents.append(application1)

        with open("job_application.json", 'w') as f:
            json.dump(contents, f)

        # Checks that the system notifies the user of how many jobs they have applied for when entering the job section
        with mock.patch('builtins.input', side_effect=['1', 'q', 'q']):
            options_screen(test_acc1, test_accounts, test_jobs)

        # Clears job_application.json of the test information
        with open("job_application.json", 'r') as f:
            contents = json.loads(f.read())

        contents.clear()

        with open("job_application.json", 'w') as f:
            json.dump(contents, f)

    # Tests Notifications for a new job posted (Global Notifications)
    def test_notification_new_job_posted(self):

        test_accs = [Account('john', 'John123!', 'John', 'Doe', is_plus=True),Account('mark', 'Mark123', 'Mark', 'Smith', is_plus=False)]
        new_test_job = Job("Mark","job_test","Test","Test","$1000")

        save_accounts_to_csv(test_accs)

        new_job_notif(test_accs[0], new_test_job.title)

        self.assertIn('A new job job_test has been posted.', get_global_notifications(test_accs[1]))

    # Tests Notifications for a deleted job (Global Notifications)
    def test_notification_deleted_applied_job(self):

        test_job = Job("mark", "job1", "description", "employer", "$1000")
        test_acc = Account('john', 'John123!', 'John', 'Doe', is_plus=True)

        job_deleted_notif(test_acc, test_job.title)

        self.assertIn('The job job1 you applied for was deleted.', get_global_notifications(test_acc))

    # Tests notifications for new student membership in Incollege. (Global Notifications)
    def test_notification_new_student_join(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe', is_plus=True)]
        new_test_acct = Account('mark', 'Mark123', 'Mark', 'Smith', is_plus=False)

        new_user_notif(test_accounts, new_test_acct)

        # Shows test account 1 that test account 2, mark smith, has joined inCollege
        self.assertIn('Mark Smith has joined InCollege.', get_global_notifications(test_accounts[0]))

    # Tests notifications to apply for a job soon after 7 days of inactivity
    def test_notifcation_apply_to_jobs_soon(self):
        test_acc1 = Account('john', 'John123!', 'John', 'Doe', is_plus=True)
        test_jobs = [Job("mark", "job1", "description", "employer", "$1000"),
                     Job("mark", "job2", "description", "employer", "$1000")]
        
        # User notifications must include "must apply to job"
        self.assertIn("Remember – you're going to want to have a job when you graduate.\n   Make sure that you start to apply for jobs today!", get_login_notifications(test_acc1))

    # Tests the notifications when a new message is received
    def test_notifcation_new_message(self):

        test_sender = Account('john', 'John123!', 'John', 'Doe')
        test_recipient = Account('mark', 'Mark123', 'Mark', 'Smith')
        test_message = "Hello Mark!"

        with mock.patch('builtins.input', side_effect=[]):
            send_message(test_sender, test_recipient.username, test_message)

        # testing for new notification
        self.assertIn('You have messages waiting for you.', get_login_notifications(test_recipient))

        # Clears the data from new_messages.json that is created when test is ran
        with open("new_messages.json", "r") as f:
            messageInfo = json.loads(f.read())

        messageInfo.clear()
        with open("new_messages.json", "w") as f:
            json.dump(messageInfo, f)

    # Tests that a user is correctly notified if they have not yet created a profile
    # And tests that the notification is NOT displayed if a user has created a profile
    def test_profile_notification(self):
        test_acc1 = Account("john", "John123!", "John", "Doe")
        test_acc2 = Account("mark", "Mark123!", "Mark", "Smith")

        test_profile = Profile(test_acc2.username, 'Student', 'CS', 'USF', 'I am 4th year student at USF')
        test_profile.write_profile_info()

        # This test checks that the notification is displayed if a profile hasn't been created
        test_notifications = get_login_notifications(test_acc1)
        print("test_acc1", test_notifications)

        # This test checks that the notification is not displayed if a profile has created
        test_notifications = get_login_notifications(test_acc2)
        print("test_acc2", test_notifications)

        # Clears profiles.json of the test information
        with open("profiles.json", 'r') as f:
            contents = json.loads(f.read())

        contents.clear()
        with open("profiles.json", 'w') as f:
            json.dump(contents, f)


if __name__ == '__main__':
    unittest.main()