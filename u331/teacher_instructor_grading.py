# Insert AP Lit & Comp rubric w/ teacher/instructor input available
print("Please grade your students test submissions below.")

print("Below is the criteria for a written thesis statement. Please grade accordingly.")
essay_score = 0.0
Thesis_grade = True
ev_and_comm = True
soph_grade = True


Thesis_grade = input("Please enter the grade for the written thesis: ")
if Thesis_grade == "0":
    print("Grade: 0")
    essay_score += 0
else:
    print("Grade: 1")
    essay_score += 1

ev_and_comm = input("Please enter the grade for evidence & commentary: ")
if ev_and_comm == "0":
    print("Grade: 0")
    essay_score += 0
elif ev_and_comm == "1":
    print("Grade: 1")
    essay_score += 1
elif ev_and_comm == "2":
    print("Grade: 2")
    essay_score += 2
elif ev_and_comm == "3":
    print("Grade: 3")
    essay_score += 3
else:
    print("Grade: 4")
    essay_score += 4


soph_grade = input("Please grade student sophistication accordingly: ")
if soph_grade == "0":
    print("Grade: 0")
    essay_score += 0
else:
    print("Grade: 1")
    essay_score += 1


print(essay_score)