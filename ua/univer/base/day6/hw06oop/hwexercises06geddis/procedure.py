class Procedure:
    def __init__(self, name_procedure, date, doctor_name, prise_procedure):
        self.__prise_procedure = prise_procedure
        self.__doctor_name = doctor_name
        self.__date = date
        self.__name_procedure = name_procedure

    def set_prise_procedure(self, prise_procedure):
        self.__prise_procedure = prise_procedure

    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    def set_date(self, date):
        self.__date = date

    def set_name_procedure(self, name_procedure):
        self.__name_procedure = name_procedure

    def get_prise_procedure(self):
        self.__prise_procedure

    def get_doctor_name(self):
        self.__doctor_name

    def get_date(self):
        self.__date

    def get_name_procedure(self):
        self.__name_procedure

    def __str__(self):
        return f"{self.__name_procedure};{self.__date};{self.__doctor_name};{self.__prise_procedure}"