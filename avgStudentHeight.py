student_heights = input("Input a list of student heights ").split()
print(student_heights)
print(type(student_heights))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
total_students = 0
for height in student_heights:
    total_height = total_height + height
    total_students = total_students + 1
average_height = round(total_height / total_students)
print(total_height)
print(total_students)
print(average_height)
