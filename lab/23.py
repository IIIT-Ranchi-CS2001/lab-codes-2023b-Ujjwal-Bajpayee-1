def classify_students():
    students = {}
    
    for _ in range(5):
        name = input("Enter student's name: ")
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks
    
    high_performers = []
    average_performers = []
    low_performers = []
    
    for name, marks in students.items():
        if marks >= 85:
            high_performers.append(name)
        elif 60 <= marks < 85:
            average_performers.append(name)
        else:
            low_performers.append(name)
    
    print(f"High Performers ({len(high_performers)}): {', '.join(high_performers)}")
    print(f"Average Performers ({len(average_performers)}): {', '.join(average_performers)}")
    print(f"Low Performers ({len(low_performers)}): {', '.join(low_performers)}")
    
    highest_marks_student = max(students, key=students.get)
    print(f"The student with the highest marks is {highest_marks_student} with {students[highest_marks_student]}%")

if __name__ == "__main__":
    classify_students()