"""_summary_

    Returns:
        _type_: _description_
    """


class UserInfo:
    """ class defining a user object
    """

    def __init__(self, username: str, email_address: str) -> None:
        self.username = username
        self.email_address = email_address

    def check_username(self, username_to_check: str) -> bool:
        """ A method that checks if the give username
            matches the actual username
        Args:
            username_to_check (str): possible username to be checked

        Returns:
            bool : True for matching name otherwise False
        """
        if username_to_check == self.username:
            return True
        else:
            return False


john = UserInfo("peezy", "j@jmail.com")
print(john.username)
print(john.email_address)
print(john.check_username("king"))
