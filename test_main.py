from main import *
import unittest
import mock
import csv
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

    # Run this test with 'jobs.txt' empty; can change assert count accordingly if testing more input
    # Test checks that the number of jobs in 'jobs.txt' matches the number of jobs created
    def test_create_jobs(self):
        with mock.patch('builtins.input', side_effect=['Software Engineer', 'Developing SW', 'Microsoft', '70000']):
            create_job('Alice')

        with mock.patch('builtins.input', side_effect=['Project Lead', 'Oversee developers', 'Google', '80000']):
            create_job('John')

        count = 0
        with open('jobs.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            try:
                for row in csv_reader:
                    count += 1
            except IndexError:
                pass

        assert count == 2


if __name__ == '__main__':
    unittest.main()

