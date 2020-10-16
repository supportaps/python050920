class personalData:

    def __init__(self):
        self.__name = None
        self.__adress = None
        self.__age = None
        self.__phone_number = None

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number


