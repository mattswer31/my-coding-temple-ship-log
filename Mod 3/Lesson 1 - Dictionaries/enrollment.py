def add_course(course):
    if course not in enrollment:
        enrollment[course] = {}
        print(f"Course: {course} added.")
    else:
        print(f"Course: {course} already exists.")

def register_student(course, student):
    if course in enrollment:
        enrollment[course][student] = True
        print(f"{student} registered for course: {course}.")
    else:
        print(f"Course: {course} does not exist.")

def remove_student(course, student):
    if course in enrollment:
        del enrollment[course][student]
        print(f"Student {student} removed from course: {course}.")
    else:
        print(f"Course: {course} or {student} not found.")

def display_courses():
    for course, students in enrollment.items():
        print(f"Course: {course}")
        for student in students:
            print(f"    Student: {student}")
            
enrollment = {"CS101" : {"Matt" : True}}
add_course("Data Structures")
register_student("Data Structures", "Matt")
display_courses()
remove_student("Data Structures", "Matt")
display_courses()
