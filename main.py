
class Student:
    age = 0
    name = ''
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def addition(self, x, y):
        if -1000 < x < 1000 and -1000 < y < 1000:
            a = x + y
            return a
        else:
            return "Не могу сложить"

    def multiplication(self, x, y):
        if -1000 < x < 1000 and -1000 < y < 1000:
            a = x * y
            return a
        else:
            return "Не могу умножить"

class Class_room_teacher:
    age = 0
    name = ''

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def set_age(self, x):
        if type(x) == int:
            self.age = x
        else:
            return "Введите число"

    def set_name(self, x):
        if type(x) == str:
            self.name = x
        else:
            return "Введите Строку"

    def get_name(self):
        return self.name


class Class:
    students = []
    letter = ''
    class_room_teacher = Class_room_teacher(0,"")
    student = Student(0,'')
    def add_student(self, student):
        self.students.append(student)


    def __init__(self, letter, students, class_room_teacher):
        self.letter = letter
        self.students = students
        self.class_room_teacher = class_room_teacher

    def set_teacher(self, name):
        self.class_room_teacher.set_name(name)

    def get_teacher(self):
        return self.class_room_teacher.get_name()


class School:
    name = ""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class preschooler:
    age = 0
    name = ''
    school = School("")

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def set_age(self, x):
        if type(x) == int:
            self.age = x
        else:
            return "Введите число"

    def set_name(self, x):
        if type(x) == str:
            self.name = x
        else:
            return "Введите Строку"

    def set_School(self, U):
        school = School(U)

    def get_School(self):
        return self.school.get_name()

    def get_preschooler(self):
        return "Меня зовут {}, мне {} лет".format(self.name, self.age)

    def addition(self, x, y):
        if 0 < x < 100 and 0 < y < 100:
            a = x + y
            return a
        else:
            return "Не могу сложить"
