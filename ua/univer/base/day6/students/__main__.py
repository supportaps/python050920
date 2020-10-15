from ua.univer.base.day6.students.group import Group


if __name__ == '__main__':
   # students = get_students_from_console()
   # write_to_file("students",students)
   group = Group()
   students = group.get_students_from_file()

   for st in students:
       if st.get_average_marks()>4:
        print(st)