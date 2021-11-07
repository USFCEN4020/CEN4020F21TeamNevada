import unittest
import mock
from account_creation import create_account
from job_class import Job
from account_class import Account
from profile_class import Profile
from profile_creation import *
from account_creation import new_user_notif
from job_apply import *
from job_deletion import *
from notifications import *

class TestCases(unittest.TestCase):
    
    def test_notification_currently_applied(self):
        pass


    def test_notification_new_job_posted(self):
        pass

    def test_notification_deleted_applied_job(self):
        pass

    # Tests notifications for new student membership in Incollege.
    def test_notification_new_student_join(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe', is_plus=True)]
        new_test_acct = Account('mark', 'Mark123', 'Mark', 'Smith', is_plus=False)

        new_user_notif(test_accounts, new_test_acct)

        # Shows test account 1 that test account 2, mark smith, has joined inCollege
        self.assertEqual(get_global_notifications(test_accounts[0]),['Mark Smith has joined InCollege.'])

    # Tests notifications to apply for a job soon after 7 days of inactivity
    def test_notifcation_apply_to_jobs_soon(self):
        test_acc1 = Account('john', 'John123!', 'John', 'Doe', is_plus=True)
        test_jobs = [Job("mark", "job1", "description", "employer", "$1000"),
                     Job("mark", "job2", "description", "employer", "$1000")]

        self.assertEqual(get_login_notifications(test_acc1),["Remember – you're going to want to have a job when you graduate.\n   Make sure that you start to apply for jobs today!"])
        

    def test_notifcation_new_message(self):
        pass

if __name__ == '__main__':
    unittest.main()