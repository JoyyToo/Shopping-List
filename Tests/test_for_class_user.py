"""Test for User class"""

import unittest
from shoppflask.user.user import User


class TestForUserClass(unittest.TestCase):
    """Test for user class"""
    def setUp(self):
        """Initializes test for user Class"""
        self.usr = User()

    # tests for signup
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.usr.register('', '', '', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result,)

    def test_for_empty_username_field(self):
        """Test for empty username field"""
        result = self.usr.register('', 'user@gmail.com', 'usrpass', 'usrpass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_empty_email_field(self):
        """Test for empty email field"""
        result = self.usr.register('user', '', 'usrpass', 'usrpass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_non_matching_passwords(self):
        """Test for non-matching passwords"""
        result = self.usr.register('user', 'user@gmail.com', 'usrpass', 'pass')
        self.assertEqual({"type": "error", "msg": "Passwords not matching"}, result)

    # tests for signin
    def test_for_empty_login_fields(self):
        """Test for empty fields"""
        result = self.usr.login('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result, )

    def test_for_empty_loginmail_field(self):
        """Test for empty email field"""
        result = self.usr.login('', 'pass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_empty_password_field(self):
        """Test for empty password field"""
        result = self.usr.login('user@gmail.com', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_wrong_password_(self):
        """Test for wrong password"""
        self.usr.login('user@gmail.com', 'pass')
        result = self.usr.login('user@gmail.com', 'pt')
        self.assertEqual({'type': 'error', 'msg': 'Incorrect credentials'}, result)

if __name__ == '__main__':
    unittest.main()
