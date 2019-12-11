class LoginData():
    """
    Set the data to use in the test
    """

    __USER = 'standard_user'
    __LOCKED_USER = 'locked_out_user'
    __PASS = 'secret_sauce'

    __LOCKED_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'

    def get_user(self):
        """Method to obtain the private variable user

        Returns:
            String -- private variable user
        """
        return self.__USER

    def get_pass(self):
        """Method to obtain the password

        Returns:
            String -- private variable password
        """
        return self.__PASS

    def get_locked_user(self):
        """Method to obtain the locked user

        Returns:
            String -- private variable locked user
        """
        return self.__LOCKED_USER

    def get_locked_message(self):
        """Method to obtain the locked message

        Returns:
            String -- Private variable locked message
        """
        return self.__LOCKED_MESSAGE
