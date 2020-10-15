import json

from ua.univer.base.day6.students.student import Student


class Group:
    def get3Students(self):
        students = []
        students.append(Student("Tom", 1))
        students.append(Student("Bob", 2))
        students.append(Student("Alice", 1))
        return students

    def get_students_from_console(self):
        students = []
        while True:
            answer = input("Enter Student [y/n]")
            if answer == "y" or answer == "Y":
                name = input("name")
                group = input("group")
                student = Student(name, group)
                student.set_mark_from_console()
                students.append(student)
            else:
                break;
        return students

    def get_students_from_file(self):
        students = []
        students_dict = self.read_from_file()
        for student_dict in students_dict:
            print(student_dict)
            student = self.create_student_from_dict(student_dict)
            students.append(student)
        return students

    def read_from_file(self):
        with open("students.json", "r") as file:
            str_json = file.read()
        mydict = json.loads(str_json)
        return mydict["students"]

    def create_student_from_dict(self, student_dict):
        student = Student(student_dict["name"], int(student_dict["group"]))
        student.set_marks(student_dict["marks"])
        return student

    def write_to_file(self, filename, students):
        dictStudents = {}
        dictStudents["students"] = []
        for student in students:
            dictStudents["students"].append(student.convert_to_dict())
        jsonData = json.dumps(dictStudents)
        print(jsonData)
        with open(filename + ".json", "w") as file:
            file.write(jsonData)