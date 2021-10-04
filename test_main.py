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
        with mock.patch('builtins.input', side_effect=['2', 'john', 'John123!', '5', 'x', '9', 'x', '1', '1', 'q', 'q', 'q']):
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


if __name__ == '__main__':
    unittest.main()
