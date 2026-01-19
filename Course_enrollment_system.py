course_enrollments = []

def enroll_course():
    student = input("Enter student name: ")
    course = input("Enter course name: ")
    course_enrollments.append({"student": student, "course": course})
    print("Enrollment successful")

def view_enrollments():
    if not course_enrollments:
        print("No enrollments available")
    else:
        for enroll in course_enrollments:
            print(enroll["student"], "- Enrolled in:", enroll["course"])

def main():
    while True:
        print("1. Enroll Course")
        print("2. View Enrollments")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            enroll_course()
        elif choice == "2":
            view_enrollments()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
