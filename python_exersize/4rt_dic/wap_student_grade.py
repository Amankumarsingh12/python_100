student_score = {
    "harry" : 81,
    "Roy"   : 78,
    "Hermione"  : 66,
    "Draco" : 74,
    "Neville"   : 93,
}

student_grade = {}

for key in student_score :
    if student_score[key] >= 91 and student_score[key] <= 100 :
        student_grade[key] = "Outstanding"
    elif student_score[key] >= 81 and student_score[key] <= 90 :
        student_grade[key] = "Exeeds Expectation"
    elif student_score[key] >= 71 and student_score[key] <= 80 :
        student_grade[key] = "Acceptable"
    elif student_score[key] <= 70 :
        student_grade[key] = "Fail"

print(student_grade,student_score)