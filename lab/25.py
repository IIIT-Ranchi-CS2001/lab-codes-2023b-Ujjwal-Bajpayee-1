# Define the sets of students
all_students = {"tom", "pikachu", "jerry", "spidey", "doreamon", "chotabheem", "Nagraj", "balveer", "motu", "patlu"}
plantation_drive = {"spidey", "motu", "patlu"}
military_exhibition = {"Nagraj", "pikachu", "spidey"}
attended_class = {"doreamon", "balveer"}

# Determine who attended both events
both_events = plantation_drive & military_exhibition

# Determine who attended only one event
only_one_event = (plantation_drive ^ military_exhibition) - attended_class

# Determine who bunked the class
bunked_class = all_students - attended_class - plantation_drive - military_exhibition

# Print the results
print("Students who attended both events:", both_events)
print("Students who attended only one event:", only_one_event)
print("Students who bunked the class:", bunked_class)