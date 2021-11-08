import unittest
import mock
from job_class import Job
from account_class import Account
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

        # Kameron's Code

        pass

    # Tests Notifications for a new job posted (Global Notifications)
    def test_notification_new_job_posted(self):

        #Kameron's Code
        pass

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


if __name__ == '__main__':
    unittest.main()