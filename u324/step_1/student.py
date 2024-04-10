from course import Course
class Student:
    student_id = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1

    def __str__(self):
        # Calling "print(student)"" from main.py will call this method instead
        # You will need to use a variable in the loop, so you must initialize it here,
        # that variable will need to be initialized to get items listed in the first def _init_ section
        # add a loop that will go through the course list
        # Add code here to create a string representation of a student,
        # including first and last name and all courses that student is taking
        info = self.last_name + ", " + self.first_name

        for course in self.courses:
            info += ", " + str(course)

        return info

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_id(self):
        return self.student_id

    def add_course(self, new_course):
        return self.courses.append(new_course)