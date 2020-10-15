import json


class Student:
    def __init__(self, name, group):
        self.__group = group
        self.__name = name
        self.__marks = [0,0,0,0,0]

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def get_count_marks(self):
        return len(self.__marks)

    def get_name(self):
        return self.__name

    def set_group(self, group):
        self.__group = group

    def get_group(self):
        return self.__group

    def set_mark(self,index, mark):
        self.__marks[index]=mark

    def get_mark(self,index):
        return self.__marks[index]

    def get_average_marks(self):
        sum=0
        for mark in self.__marks:
            sum+= mark
        return sum/len(self.__marks)

    def write_to_file(self,filename):
        jsonData = self.convert_to_json()
        with open(filename + ".json", "a") as file:
            file.write(jsonData)

    def convert_to_json(self):
        dictData = self.convert_to_dict()
        jsonData = json.dumps(dictData)
        print(jsonData)
        return jsonData

    def convert_to_dict(self):
        dictData = {}
        dictData["name"] = self.get_name()
        dictData["group"] = self.get_group()
        dictData["marks"] = self.get_marks()
        return dictData

    def set_mark_from_console(self):
        for i in range(self.get_count_marks()):
            mark = int(input(f"Enter {i} mark "))
            self.set_mark(i, mark)

    def __str__(self):
        return f"Student;{self.__name};{self.__group};{self.__marks}"