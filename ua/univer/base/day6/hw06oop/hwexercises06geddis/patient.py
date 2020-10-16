class Patient:
    def __init__(self, name, address, phone_number, name_and_phone_assistant):

        self.__name_and_phone_assistant = name_and_phone_assistant
        self.__phone_number = phone_number
        self.__address = address
        self.__name = name



    def set_name_and_phone_assistant(self, name_and_phone_assistant):
        self.__name_and_phone_assistant = name_and_phone_assistant

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def set_name(self, name):
        self.__name = name


    def get_name_and_phone_assistant(self):
        return self.__name_and_phone_assistant

    def get_phone_number(self):
        return  self.__phone_number

    def get_address(self):
        return self.__address

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name};{self.__address};{self.__phone_number};{self.__name_and_phone_assistant}"