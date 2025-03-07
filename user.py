class User:
    def __init__(self):
        self.__fullname = None
        self.__email = None
        self.__password = None

    def set_name(self, fullname):
        self.__fullname = fullname
    def set_email(self, email):
        self.__email = email
    def set_password(self, password):
        self.__password = password
    def get_name(self):
        return self.__fullname
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password



