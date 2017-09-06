"""User class"""


class User(object):
    """User class"""
    user = {}

    def __init__(self):
        """Initializes the class """

    def register(self, name, passwd, cpasswd, email):
        """Registers user"""
        if name and passwd and email and cpasswd:
            msg = {
                "type": "error",
                "msg": "Passwords not matching"
            }
            if passwd == cpasswd:

                new_user = {
                    "name": name,
                    "pass": passwd,
                    "email": email,
                    "cpasswd": cpasswd
                }

                self.user[email] = new_user

                return {
                    "type": "success",
                    "msg": "You have registered successfully"
                }
            return msg

        else:
            return {
                "type": "error",
                "msg": "Please Fill all the fields"
            }

    def login(self, passwd, email):
        """Enables user login"""
        if email and passwd:
            msg = {
                "type": "error",
                "msg": "Incorrect credentials"
            }
            if email in self.user.keys():
                if self.user[email]['pass'] == passwd:
                    return {
                        "type": "success",
                        "msg": "You have successfully logged in",
                        "user_detail": {
                            "name": self.user[email]["name"],
                            "email": self.user[email]['email']
                        }
                    }
                return msg
            return msg

        else:
            return {
                "type": "error",
                "msg": "Please Fill all the fields"
            }
