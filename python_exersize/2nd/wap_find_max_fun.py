student_score=input("enter score of student ").split()

max=0

for n in student_score:
    n1=int(n)
    if n1>max:
        max=n1

print(max)