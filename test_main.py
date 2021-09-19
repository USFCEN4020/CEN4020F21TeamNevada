from main import *
import unittest


class TestCases(unittest.TestCase):
    def test_login_screen(self, ):
        names = ['alice', 'lily']
        passwords = ['Alice123!', 'J!888888']
        assert passwd_valid(names, passwords, 'alice', 'Alice123!')
        assert not passwd_valid(names, passwords, 'alice', 'Alice')
        assert passwd_valid(names, passwords, 'lily', 'J!888888')
        assert not passwd_valid(names, passwords, 'lily', 's888')
        assert not passwd_valid(names, passwords, 'lily', '')

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


if __name__ == '__main__':
    unittest.main()

