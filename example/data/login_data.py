class LoginData():
    __USER = 'standard_user'
    __LOCKED_USER = 'locked_out_user'
    __PASS = 'secret_sauce'

    __LOCKED_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'

    def get_user(self):
        return self.__USER

    def get_pass(self):
        return self.__PASS

    def get_locked_user(self):
        return self.__LOCKED_USER

    def get_locked_message(self):
        return self.__LOCKED_MESSAGE
