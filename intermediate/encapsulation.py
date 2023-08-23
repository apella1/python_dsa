class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    def check_username(self, username_to_check):
        if username_to_check == self.username:
            return True
        else:
            return False


john = UserInfo("peezy", "j@jmail.com")
print(john.username)
print(john.email_address)
print(john.check_username("king"))
