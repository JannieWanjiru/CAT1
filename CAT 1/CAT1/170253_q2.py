class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}
        

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' added with grade {grade} for {self.name}.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"  - {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_grades(self):
        if self.students:
            print(f"Grades for all students in {self.course_name}:")
            for student in self.students:
                student.display_grades()
        else:
            print("No students in the course.")

# Sample functionality
instructor = Instructor("Dr. Smith", "Introduction to Python")

def course_management_system():
    while True:
        print("\nOptions: 1) Add Student 2) Assign Grade 3) Display All Grades 4) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "3":
            instructor.display_all_students_grades()

        elif choice == "4":
            print("Exiting the course management system.")
            break
        else:
            print("Invalid option, please try again.")


