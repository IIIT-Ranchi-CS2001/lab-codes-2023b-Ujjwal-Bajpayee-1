course_codes = ["CS1001", "CS2002", "MA3003", "EN4004", "ST5005"]
course_names = ["Python", "Data Structures", "Calculus", "English Literature", "Statistics"]

combined_list = list(zip(course_codes, course_names))

combined_list_formatted = [f"{code}: {name}" for code, name in combined_list]

print("Combined List:")
for course in combined_list_formatted:
    print(f"* {course}")