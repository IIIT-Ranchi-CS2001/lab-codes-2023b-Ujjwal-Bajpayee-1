names = [f"Student{i}" for i in range(1, 11)]
roll_nos = [i for i in range(1, 11)]
marks = [75 + i for i in range(10)]

students = []
for i in range(10):
    students.append((names[i], roll_nos[i], marks[i]))

sorted_students = sorted(students, key=lambda student: student[2])

for student in sorted_students:
    print(student)