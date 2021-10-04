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

        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 'l', 'mark', 'Mark123!', 'q']):
            main_screen(test_accounts)

        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 's', 'sally', 'Hill123!', 'Sally', 'Hill',
                                                       'sally', 'Hill123!', 'q']):
            main_screen(test_accounts)

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


if __name__ == '__main__':
    unittest.main()
