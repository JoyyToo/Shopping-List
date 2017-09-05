import unittest
from shoppflask.user.user import User


class TestForUserClass(unittest.TestCase):
    def setUp(self):
        self.usr = User()

    # tests for signup
    def test_for_empty_fields(self):
        result = self.usr.register('', '', '', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result,)

    def test_for_empty_username_field(self):
        result = self.usr.register('', 'user@gmail.com', 'usrpass', 'usrpass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_empty_email_field(self):
        result = self.usr.register('user', '', 'usrpass', 'usrpass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_non_matching_passwords(self):
        result = self.usr.register('user', 'user@gmail.com', 'usrpass', 'pass')
        self.assertEqual({"type": "error", "msg": "Passwords not matching"}, result)

    # tests for signin
    def test_for_empty_login_fields(self):
        result = self.usr.login('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result, )

    def test_for_empty_email_login_field(self):
        result = self.usr.login('', 'pass')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_empty_password_field(self):
        result = self.usr.login('user@gmail.com', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_wrong_password_(self):
        self.usr.login('user@gmail.com', 'pass')
        result = self.usr.login('user@gmail.com', 'pt')
        self.assertEqual({
                'type': 'error',
                'msg': 'Incorrect credentials'
            }, result)
if __name__ == '__main__':
    unittest.main()




