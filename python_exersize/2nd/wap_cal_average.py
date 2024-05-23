
#.split() use to convert a series of input to a list
#.split(,) divide it series with delimeter of ,
student_height=input("enter height ").split()

#print(student_height)

length=0;sum=0;avg=0;

for sum_in in student_height:
    sum += int(sum_in)
    length +=1

avg = sum / length



print(f"average height is {round(avg)}")
