from main import *
import unittest
import mock
from account_class import Account
from account_login import login_screen
from show_network import show_network
from job_deletion import delete_job
from job_apply import apply_job
from job_class import Job
from unittest import mock
from account_class import Account
from job_apply import *
from send_message import *
from view_message import *
from learning import *

class TestCases(unittest.TestCase):
    def test_login_screen(self, ):
        test_accounts = [Account('alice', 'Alice123!'), Account('lily', 'J!888888')]
        assert passwd_valid(test_accounts, 'alice', 'Alice123!')
        assert not passwd_valid(test_accounts, 'alice', 'Alice')
        assert passwd_valid(test_accounts, 'lily', 'J!888888')
        assert not passwd_valid(test_accounts, 'lily', 's888')
        assert not passwd_valid(test_accounts, 'lily', '')

    def test_is_secure(self, ):
        condition, message = is_secure('123')
        assert not condition
        assert message == 'Error: password must be a minimum of 8 and a maximum of 12 characters'
        condition, message = is_secure('12345678')
        assert not condition
        assert message == "Error: password must contain at least 1 capital letter"
        condition, message = is_secure('ABCDEFGHI')
        assert not condition
        assert message == "Error: password must contain at least 1 digit"
        condition, message = is_secure('ab123C...')
        assert condition and message == ''

    # Tests the three options that users are presented with when connecting with friends ('l', 's', 'q')
    def test_main_screen(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        print("-----TEST OPTION 'l'-----")
        with mock.patch('builtins.input',
                        side_effect=['3', 'John', 'Doe', 'l', 'mark', 'Mark123!', 'q']):
            main_screen(test_accounts)

        print("-----TEST OPTION 's'-----")
        with mock.patch('builtins.input',
                        side_effect=['3', 'John', 'Doe', 's', 'sally', 'Hill123!', 'Sally', 'Hill', "1",
                                     'sally', 'Hill123!', 'q']):
            main_screen(test_accounts)

        print("-----TEST OPTION 'q'-----")
        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 'q', 'q']):
            main_screen(test_accounts)

    # Tests if the input first and last name are in the InCollege database
    def test_connect_with_users(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        with mock.patch('builtins.input', side_effect=['John', 'Doe', 'Sally', 'Hill']):
            result = connect_with_users(test_accounts)
            assert result

            result = connect_with_users(test_accounts)
            assert not result

    # Tests that 'user_exists' functions correctly
    def test_user_exists(self, ):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]
        condition = user_exists(test_accounts, 'Mark', 'Smith')
        assert condition
        condition = user_exists(test_accounts, 'John', 'Doe')
        assert condition
        condition = user_exists(test_accounts, 'Sally', 'Hill')
        assert not condition
        condition = user_exists(test_accounts, 'John', 'Smith')
        assert not condition

    # Tests that the success story is displayed and tests the two options users are presented with on the home screen
    def test_home_screen(self):
        with mock.patch('builtins.input', side_effect=['1', '\n', 'x', '2']):
            home_screen()

    # Tests the first option (general links) of the useful links functionality
    def test_useful_links_groups_option1(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # This test additionally checks to make sure that invalid user input is handled correctly (i.e user inputs 'x')
        print("-----TEST_OPTION 1.1-----")
        with mock.patch('builtins.input',
                        side_effect=['4', 'x', '1', 'x', '1', 'sally', 'Hill123!', 'Sally', 'Hill', "1",
                                     'sally', 'Hill123!', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.2-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '2', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.3-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '3', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.4-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '4', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.5-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '5', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.6-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '6', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 1.7-----")
        with mock.patch('builtins.input', side_effect=['4', '1', '7', 'q', 'q', 'q']):
            main_screen(test_accounts)

    # Tests options 2 through 4 of the useful links functionality
    def test_useful_links_groups_options2_thru_4(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # This test additionally checks to make sure that invalid user input is handled correctly (i.e user inputs 'x')
        print("-----TEST_OPTION 2-----")
        with mock.patch('builtins.input', side_effect=['4', 'x', '2', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 3-----")
        with mock.patch('builtins.input', side_effect=['4', '3', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 4-----")
        with mock.patch('builtins.input', side_effect=['4', '4', 'q', 'q']):
            main_screen(test_accounts)

    # Tests that each guest control can be properly enabled and disabled
    def test_guest_controls(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # This test additionally checks to make sure that invalid user input is handled correctly (i.e user inputs 'x')
        print("-----TEST_OPTION 1-----")
        with mock.patch('builtins.input',
                        side_effect=['2', 'john', 'John123!', '5', 'x', '9', 'x', '1', '1', 'q',
                                     'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 2-----")
        with mock.patch('builtins.input',
                        side_effect=['2', 'john', 'John123!', '5', '9', '2', '2', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 3-----")
        with mock.patch('builtins.input',
                        side_effect=['2', 'john', 'John123!', '5', '9', '3', '3', 'q', 'q', 'q']):
            main_screen(test_accounts)

        # This test checks that 'enable all' and 'disable all' work correctly
        print("-----TEST_OPTIONS 'd'+'e'-----")
        with mock.patch('builtins.input',
                        side_effect=['2', 'john', 'John123!', '5', '9', 'd', 'e', 'q', 'q', 'q']):
            main_screen(test_accounts)

    # Tests to make sure the important links are displayed when logged-in and logged-out
    def test_important_links(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # Tests links without login
        with mock.patch('builtins.input',
                        side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'q']):
            important_links_groups(False)

        # Tests links with login information with 1 link
        with mock.patch('builtins.input',
                        side_effect=['john', 'John123!', '1', '2', '3', '4', '5', '6', '7', '8',
                                     'q']):
            user = login_screen(test_accounts)
            important_links_groups(user, test_accounts)

        # Tests Language options in important links while logged in
        with mock.patch('builtins.input',
                        side_effect=['john', 'John123!', '10', '2', 'q', '10', '1', 'q', 'q']):
            user = login_screen(test_accounts)
            important_links_groups(user, test_accounts)

    # Tests creating a profile
    def test_profile_creation(self):
        test_account = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input',
                        side_effect=['test title', 'test major', 'test university', 'test about',
                                     'y', 'test job title', 'test employer', 'test start date',
                                     'test end date', 'test location', 'test job description', 'n',
                                     'test school name', 'test degree', '5 years', 'n']):
            profile_creation(test_account)

    # Tests retrieving the profile information
    def test_get_profile_info(self):
        test_account = Account('mark', 'Mark123!', 'Mark', 'Smith')
        with mock.patch('builtins.input',
                        side_effect=['test title', 'test major', 'test university', 'test about',
                                     'y', 'test job title', 'test employer', 'test start date',
                                     'test end date', 'test location', 'test job description', 'n',
                                     'test school name', 'test degree', '5 years', 'n']):
            profile_creation(test_account)

        test_profile_obj = Profile()
        # tests the profile was created by checking the number of profiles
        assert len(test_profile_obj.get_profile_list()) > 0

        # tests the get profile info to ensure that it is retrieving the correct profile info
        test_profile_info = test_profile_obj.get_profile_info(test_account.username)
        test_job_info = {
            "job_name": "test job title",
            "employer": "test employer",
            "start_date": "test start date",
            "end_date": "test end date",
            "location": "test location",
            "description": "test job description"
        }
        test_education_info = {
            "school": "test school name",
            "degree": "test degree",
            "year": "5 years"
        }

        # test profile exists
        assert test_profile_info is not None

        # test basic profile information is the same as what was passed as input
        print(test_profile_info)
        assert test_profile_info['username'] == test_account.username
        assert test_profile_info['title'] == 'test title'
        assert test_profile_info['about'] == 'test about'

        # test basic profile information with capitalization formatting
        assert test_profile_info['major'] == 'Test Major'  # was in all lowercase in input
        assert test_profile_info['university'] == 'Test University'  # was in all lowercase in input

        # test the profile job information is the same as what was passed as input
        assert len(test_profile_info['jobs']) > 0
        assert test_profile_info['jobs'][0] == test_job_info

        # test the profile education information is the same as what was passed as input
        assert len(test_profile_info['education']) > 0
        assert test_profile_info['education'][0] == test_education_info

        # test the get profile info returns None when a profile does not exist with the given username
        assert test_profile_obj.get_profile_info("random account username") is None

    # Tests network
    def test_show_network(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # Tests links with log in information with 1 link
        with mock.patch('builtins.input',
                        side_effect=['john', 'John123!', '1', '2', 'q']):
            user = login_screen(test_accounts)
            show_network(user)

    # Test search for students
    def test_student_friend_connections(self):
        # check to see if the test accounts john and mark have been created
        accounts = get_accounts_from_csv()
        if len(accounts) < 1:
            print("\n** Creating test accounts using the test important links test **")
            self.test_important_links()  # this test creates the test accounts for john and mark
        elif not (user_exists(accounts, "John", "Doe") and user_exists(accounts, "Mark", "Smith")):
            print("\n** Creating test accounts using the test important links test **")
            self.test_important_links()  # this test creates the test accounts for john and mark

        # check to see if the profiles for these two accounts exist
        test_account1 = Account('john', 'John123!', 'John', 'Doe')
        test_account2 = Account('mark', 'Mark123!', 'Mark', 'Smith')
        accounts = [test_account1, test_account2]

        test_profile_obj = Profile()
        # if their profiles don't exist, run the tests that create them
        if test_profile_obj.get_profile_info(test_account1.username) == None:
            print("\n** Creating test profile for John using the test profile creation test **")
            self.test_profile_creation()

        if test_profile_obj.get_profile_info(test_account2.username) == None:
            print("\n** Creating test profile for Mark using the test get profile info test **")
            self.test_get_profile_info()

        # once we have created the accounts and the profiles to test with, now we can test search students

        # test search students by last name
        with mock.patch('builtins.input',
                        side_effect=['last name', 'Smith', 'mark', 'Oh, Hi Mark']):
            connection = search_students(test_account1, accounts)
            assert connection["username"] == "john"
            assert connection["c_user"] == "mark"
            assert connection["content"] == "Oh, Hi Mark"

        # test search students by university
        with mock.patch('builtins.input',
                        side_effect=['university', 'Test University', 'mark', 'Oh, Hi Mark']):
            connection = search_students(test_account1, accounts)
            assert connection["username"] == "john"
            assert connection["c_user"] == "mark"
            assert connection["content"] == "Oh, Hi Mark"

        # test search students by major
        with mock.patch('builtins.input',
                        side_effect=['major', 'Test Major', 'mark', 'Oh, Hi Mark']):
            connection = search_students(test_account1, accounts)
            assert connection["username"] == "john"
            assert connection["c_user"] == "mark"
            assert connection["content"] == "Oh, Hi Mark"

        # test search for student that does not exist
        with mock.patch('builtins.input',
                        side_effect=['last name', 'nothing']):
            connection = search_students(test_account1, accounts)
            assert connection == None

    # Tests that the send_message function correctly stores this message info in new_messages.json
    # And that messages can be retrieved from new_messages.json
    def test_send_message(self):
        test_sender = Account('john', 'John123!', 'John', 'Doe')
        test_recipient = Account('mark', 'Mark123', 'Mark', 'Smith')
        test_message = "Hello Mark!"

        with mock.patch('builtins.input', side_effect=[]):
            send_message(test_sender, test_recipient.username, test_message)

        # Function from view_message.py
        sent_message = get_new_messages(test_recipient)

        assert sent_message[0]["sender"] == test_sender.username
        assert sent_message[0]["recipient"] == test_recipient.username
        assert sent_message[0]["message"] == test_message

        # Clears the data from new_messages.json that is created when test is ran
        with open("new_messages.json", "r") as f:
            messageInfo = json.loads(f.read())

        messageInfo.clear()
        with open("new_messages.json", "w") as f:
            json.dump(messageInfo, f)

    # Tests that new messages are displayed to the user
    # Also tests that unsaved new messages are deleted properly
    def test_view_new_message(self):
        test_sender = Account('john', 'John123!', 'John', 'Doe')
        test_recipient = Account('mark', 'Mark123', 'Mark', 'Smith')
        test_message1 = "Hello Mark!"
        test_message2 = "How are you?"

        send_message(test_sender, test_recipient.username, test_message1)
        send_message(test_sender, test_recipient.username, test_message2)
        sent_messages = get_new_messages(test_recipient)

        # delete_new_messages is called when user doesn't choose to save a new message and enters 'q'
        # Also tests invalid input i.e 'x'
        with mock.patch('builtins.input', side_effect=['x', 'q']):
            view_new_messages(test_recipient, sent_messages)

    # Tests that new messages can be saved and are correctly stored in saved_messages.json
    # And that saved messages can be retrieved and viewed/deleted from saved_messages.json
    def test_view_saved_messages(self):
        test_sender = Account('john', 'John123!', 'John', 'Doe')
        test_recipient = Account('mark', 'Mark123', 'Mark', 'Smith')
        test_message1 = "Hello Mark!"
        test_message2 = "How are you?"
        test_message3 = "I got the job!"

        send_message(test_sender, test_recipient.username, test_message1)
        send_message(test_sender, test_recipient.username, test_message2)
        send_message(test_sender, test_recipient.username, test_message3)
        sent_messages = get_new_messages(test_recipient)

        # Tests that 1 or more new messages can be saved
        # Also tests invalid input i.e 'x'
        with mock.patch('builtins.input', side_effect=['x', '1', '2', 'q']):
            view_new_messages(test_recipient, sent_messages)

        saved_message = get_saved_messages(test_recipient)

        assert saved_message[0]["sender"] == test_sender.username
        assert saved_message[0]["recipient"] == test_recipient.username
        assert saved_message[0]["message"] == test_message1

        # delete_saved_messages is called when the user chooses a message number to delete; in this case message #1
        # Also tests invalid input i.e 'x'
        with mock.patch('builtins.input', side_effect=['x', '1', 'q']):
            view_saved_messages(test_recipient, saved_message)

        # Clears the data from saved_messages.json that is created when test is ran
        with open("saved_messages.json", "r") as f:
            messageInfo = json.loads(f.read())

        messageInfo.clear()
        with open("saved_messages.json", "w") as f:
            json.dump(messageInfo, f)

    # Tests that plus members can send messages to people not in their friends list
    # And that standard members cannot
    def test_standard_plus(self):
        test_acc1 = Account('john', 'John123!', 'John', 'Doe', is_plus=True)    # plus member
        test_acc2 = Account('mark', 'Mark123', 'Mark', 'Smith', is_plus=False)  # standard member
        test_acc3 = Account('sally', 'Sally123!', 'Sally', 'Hill', is_plus=False)   # extra third member

        test_accounts_list = [test_acc1, test_acc2, test_acc3]

        john_f_list = {
            "user": test_acc1.username,
            "friends": ["mark"]
        }

        mark_f_list = {
            "user": test_acc2.username,
            "friends": ["john"]
        }

        # Adds the test friend lists to friends_list.json
        with open("friends_list.json", 'r') as f:
            friends_lists = json.loads(f.read())

        friends_lists.append(john_f_list)
        friends_lists.append(mark_f_list)

        with open("friends_list.json", 'w') as f:
            json.dump(friends_lists, f)

        # Tests that a plus member can messages anyone
        with mock.patch('builtins.input', side_effect=['sally', 'hello', 'y', 'quit']):
            send_message_ui(test_acc1, test_accounts_list)

        # Tests that a standard member cannot message someone outside their friend list
        with mock.patch('builtins.input', side_effect=['sally', 'quit']):
            send_message_ui(test_acc2, test_accounts_list)

        # Clears the data from new_messages.json that is created when test is ran
        with open("new_messages.json", "r") as f:
            messageInfo = json.loads(f.read())

        messageInfo.clear()
        with open("new_messages.json", "w") as f:
            json.dump(messageInfo, f)

        # Clears the data from friends_list.json that is created when test is ran
        with open("friends_list.json", "r") as f:
            contents = json.loads(f.read())

        contents.clear()
        with open("friends_list.json", "w") as f:
            json.dump(messageInfo, f)


    def test_learning_ui(self):
        user = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '1', 'Y', '2', 'n', 'q']):
            learning_ui(user)

        # assert len(get_user_courses(user)) == 5

    def test_businessAnalytics_options(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # Test Business and Analyitics Training Options.
        with mock.patch('builtins.input', side_effect=['6','3','q','q','q']):
            main_screen(test_accounts, jobs=[])

        # Test "How to use In College learning" Option
        with mock.patch('builtins.input', side_effect=['6','3','1','john','John123!', 'q', 'q', 'q']):
            main_screen(test_accounts, jobs=[])

        # Test the "Train the trainer" Option
        with mock.patch('builtins.input', side_effect=['6','3','2','john','John123!', 'q', 'q', 'q']):
            main_screen(test_accounts, jobs=[])

        # Test the "Gamification of learning" Option
        with mock.patch('builtins.input', side_effect=['6','3','3','john','John123!', 'q', 'q', 'q']):
            main_screen(test_accounts, jobs=[])

    def test_IT_Security_option(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        #Test the IT Help desk Option
        with mock.patch('builtins.input', side_effect=['6','2','q','q']):
            main_screen(test_accounts, jobs=[])

        #Test the Security Options
        with mock.patch('builtins.input', side_effect=['6','4','q','q']):
            main_screen(test_accounts, jobs=[])

    def test_learning_options(self):

        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                         Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # Test "InCollege Learning" options
        with mock.patch('builtins.input', side_effect=['6','1','1','2','3','4','q','q','q']):
            main_screen(test_accounts, jobs=[])


if __name__ == '__main__':
    unittest.main()
