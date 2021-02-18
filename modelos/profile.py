

class Perfil:

    def __init__(self):
        self.__login = 'admin'
        self.__password = 'admin'

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password
