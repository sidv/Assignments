class User:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        self._role = ""

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
