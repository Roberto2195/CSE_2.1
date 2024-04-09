from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")

comp_graphics = Course("Computer Graphics I")
ap_lit_and_comp = Course("AP Literature & Composition")

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("John", "Doe")
test_student3.add_course(math)
test_student3.add_course(phys_ed)
test_student3.add_course(science)
test_student3.add_course(history)
test_student3.add_course(comp_graphics)
test_student3.add_course(ap_lit_and_comp)

roster = []
roster.append(test_student)
roster.append(test_student2)
roster.append(test_student3)

for student in roster:
    print(student)

