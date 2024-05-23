import random

names = ["aman", "subham", "kumar", "ran", "alex"]

stu_dict = {student:random.randint(1, 100) for student in names}

stu_pass = {student:score for (student, score) in stu_dict.items() if score >= 60}

print( stu_dict)
print( stu_pass)

