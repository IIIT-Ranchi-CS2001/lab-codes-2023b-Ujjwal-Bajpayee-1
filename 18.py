# List of students with their skills
students = [
    {"name": "John", "skills": ["singing", "dancing"]},
    {"name": "Alice", "skills": ["singing"]},
    {"name": "Bob", "skills": ["dancing"]},
    {"name": "Charlie", "skills": ["singing", "dancing"]},
    {"name": "David", "skills": ["singing"]},
    {"name": "Eve", "skills": ["dancing"]}
]

s = {student["name"] for student in students if "singing" in student["skills"]}
d = {student["name"] for student in students if "dancing" in student["skills"]}

all_artists = s.union(d)
allrounders = s.intersection(d)
dancers_not_singers = d.difference(s)
singers_not_dancers = s.difference(d)
dancers_not_singers_cum_singers_not_dancers = d.symmetric_difference(s)

print("All Artists:", all_artists)
print("Allrounders:", allrounders)
print("Dancers but not Singers:", dancers_not_singers)
print("Singers but not Dancers:", singers_not_dancers)
print("Dancers but not Singers cum Singers but not Dancers:", dancers_not_singers_cum_singers_not_dancers)