from main import *
import unittest
import mock
from account_class import Account


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
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

        print("-----TEST OPTION 'l'-----")
        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 'l', 'mark', 'Mark123!', 'q']):
            main_screen(test_accounts)

        print("-----TEST OPTION 's'-----")
        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 's', 'sally', 'Hill123!', 'Sally', 'Hill',
                                                       'sally', 'Hill123!', 'q']):
            main_screen(test_accounts)

        print("-----TEST OPTION 'q'-----")
        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 'q', 'q']):
            main_screen(test_accounts)

    # Tests if the input first and last name are in the InCollege database
    def test_connect_with_users(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

        with mock.patch('builtins.input', side_effect=['John', 'Doe', 'Sally', 'Hill']):
            result = connect_with_users(test_accounts)
            assert result

            result = connect_with_users(test_accounts)
            assert not result

    # Tests that 'user_exists' functions correctly
    def test_user_exists(self, ):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]
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
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # This test additionally checks to make sure that invalid user input is handled correctly (i.e user inputs 'x')
        print("-----TEST_OPTION 1.1-----")
        with mock.patch('builtins.input', side_effect=['4', 'x', '1', 'x', '1', 'sally', 'Hill123!', 'Sally', 'Hill',
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
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

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
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # This test additionally checks to make sure that invalid user input is handled correctly (i.e user inputs 'x')
        print("-----TEST_OPTION 1-----")
        with mock.patch('builtins.input',
                        side_effect=['2', 'john', 'John123!', '5', 'x', '9', 'x', '1', '1', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 2-----")
        with mock.patch('builtins.input', side_effect=['2', 'john', 'John123!', '5', '9', '2', '2', 'q', 'q', 'q']):
            main_screen(test_accounts)

        print("-----TEST_OPTION 3-----")
        with mock.patch('builtins.input', side_effect=['2', 'john', 'John123!', '5', '9', '3', '3', 'q', 'q', 'q']):
            main_screen(test_accounts)

        # This test checks that 'enable all' and 'disable all' work correctly
        print("-----TEST_OPTIONS 'd'+'e'-----")
        with mock.patch('builtins.input', side_effect=['2', 'john', 'John123!', '5', '9', 'd', 'e', 'q', 'q', 'q']):
            main_screen(test_accounts)

    # Tests to make sure the important links are displayed when logged-in and logged-out
    def test_important_links(self):
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'), Account('mark', 'Mark123!', 'Mark', 'Smith')]

        # Tests links without login
        with mock.patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'q']):
            important_links_groups(False)

        # Tests links with login information with 1 link
        with mock.patch('builtins.input',
                        side_effect=['john', 'John123!', '1', '2', '3', '4', '5', '6', '7', '8', 'q']):
            user = login_screen(test_accounts)
            important_links_groups(user, test_accounts)

        # Tests Language options in important links while logged in
        with mock.patch('builtins.input', side_effect=['john', 'John123!', '10', '2', 'q', '10', '1', 'q', 'q']):
            user = login_screen(test_accounts)
            important_links_groups(user, test_accounts)

    # Tests creating a profile
    def test_profile_creation(self):
        test_account = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input',
                        side_effect=['test title', 'test major', 'test university', 'test about',
                                     'y', 'test job title', 'test employer', 'test start date', 'test end date', 'test location', 'test job description', 'n',
                                     'test school name', 'test degree', '5 years', 'n']):
            profile_creation(test_account)

    # Tests retrieving the profile information
    def test_get_profile_info(self):
        test_account = Account('mark', 'Mark123!', 'Mark', 'Smith')
        with mock.patch('builtins.input',
                        side_effect=['test title', 'test major', 'test university', 'test about',
                                     'y', 'test job title', 'test employer', 'test start date', 'test end date', 'test location', 'test job description', 'n',
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


if __name__ == '__main__':
    unittest.main()
