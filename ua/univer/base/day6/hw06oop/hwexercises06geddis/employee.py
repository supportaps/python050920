class Employee:

    def __init__(self, name, id, department, position):
        self.__position = position
        self.__department = department
        self.__id = id
        self.__name = name

    def set_position(self, position):
        self.__position = position

    def set_department(self, department):
        self.__department = department

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_id(self):
        return self.__id

    def get_position(self):
        return self.__position
