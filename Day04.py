# Store immutable student IDs using a tuple
student_ids = ("S101", "S102", "S103")

# Create a set of unique course names
courses = {"Python", "AI", "ML"}

# Add a new course to the set
courses.add("Data Science")  

# Remove a course from the set
courses.remove("AI")  

# Display student IDs
print("Student IDs:")
for sid in student_ids:
    print(sid)

# Display updated set of courses
print("\nAvailable Courses:")
for course in courses:
    print(course)