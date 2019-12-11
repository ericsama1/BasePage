class CheckoutData():
    __NAME = 'asd'
    __LAST_NAME = 'adzxczx'
    __POSTAL_CODE = 'sadasdasda'

    # Message
    __FIRSTNAME_ERROR = "Error: First Name is required"
    __LASTNAME_ERROR = "Error: Last Name is required"
    __POSTAL_ERROR = "Error: Postal Code is required"

    # GETS

    def get_name(self):
        return self.__NAME

    def get_last_name(self):
        return self.__LAST_NAME

    def get_postal_code(self):
        return self.__POSTAL_CODE

    def get_firstname_error(self):
        return self.__FIRSTNAME_ERROR

    def get_lastname_error(self):
        return self.__LASTNAME_ERROR

    def get_postal_error(self):
        return self.__POSTAL_ERROR
