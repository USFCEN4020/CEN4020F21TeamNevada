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

    # Tests that the entered first and last name are added to the InCollege database when creating an account
    # Can check 'accounts.txt' for verification
    def test_create_account(self):
        test_account = []
        with mock.patch('builtins.input', side_effect=['john', 'John123!', 'John', 'Doe']):
            create_account(test_account)

        count = 0
        with open('accounts.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            try:
                for row in csv_reader:
                    if row[2] == 'Doe' and row[3] == 'John':
                        count += 1
            except IndexError:
                pass

        assert count == 1


if __name__ == '__main__':
    unittest.main()

