import pickle

class Course:
    def _init_(self, code, name, number, core):
        self.code = code
        self.name = name
        self.number = number  # Number of credit hours
        self.core = core

    def _str_(self):
        return f"{self.code}: {self.name} ({self.number} credits) {'[Core]' if self.core else '[Elective]'}"


class Student:
    def _init_(self, ID, name):
        self.ID = ID
        self.name = name
        self.courses = {}

    def add_course(self, course):
        if course.code in self.courses:
            raise Exception(f"{self.name} is already enrolled in {course.name}.")
        self.courses[course.code] = course

    def drop_course(self, course_code):
        if course_code not in self.courses:
            raise Exception(f"{self.name} is not enrolled in {course_code}.")
        del self.courses[course_code]

    def list_courses(self):
        return [str(course) for course in self.courses.values()]


class Catalog:
    def _init_(self):
        self.courses = {}
        self.students = {}

    def add_course(self, code, name, number, core):
        if code in self.courses:
            print(f"Course with code {code} already exists.")
            return
        course = Course(code, name, number, core)
        self.courses[code] = course
        print(f"Added course: {course}")

    def enroll_student(self, student_id, student_name, course_code):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, student_name)
        student = self.students[student_id]
        if course_code not in self.courses:
            print(f"Course {course_code} does not exist.")
            return
        course = self.courses[course_code]
        try:
            student.add_course(course)
            print(f"Enrolled {student.name} in {course.name}.")
        except Exception as e:
            print(e)

    def drop_course(self, student_id, course_code):
        if student_id not in self.students:
            print(f"Student {student_id} does not exist.")
            return
        student = self.students[student_id]
        try:
            student.drop_course(course_code)
            print(f"Dropped course {course_code} for {student.name}.")
        except Exception as e:
            print(e)

    def list_student_courses(self, student_id):
        if student_id not in self.students:
            print(f"Student {student_id} does not exist.")
            return
        student = self.students[student_id]
        courses = student.list_courses()
        if not courses:
            print(f"No courses enrolled for {student.name}.")
        else:
            print(f"Courses for {student.name}:")
            for course in courses:
                print(course)

    def save_course_catalog(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.courses, self.students), f)
            print("Course catalog saved.")

    def load_course_catalog(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.courses, self.students = pickle.load(f)
                print("Course catalog loaded.")
        except Exception as e:
            print(f"Error loading catalog: {e}")

    def menu(self):
        while True:
            print("\nUniversity Course Catalog")
            print("1. Add Course")
            print("2. Enroll Student in Course")
            print("3. Drop Course for Student")
            print("4. List Student Courses")
            print("5. Save Course Catalog")
            print("6. Load Course Catalog")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                code = input("Enter course code: ")
                name = input("Enter course name: ")
                number = int(input("Enter credit hours: "))
                core = input("Is it a core course? (yes/no): ").strip().lower() == 'yes'
                self.add_course(code, name, number, core)

            elif choice == '2':
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                course_code = input("Enter course code: ")
                self.enroll_student(student_id, student_name, course_code)

            elif choice == '3':
                student_id = input("Enter student ID: ")
                course_code = input("Enter course code to drop: ")
                self.drop_course(student_id, course_code)

            elif choice == '4':
                student_id = input("Enter student ID: ")
                self.list_student_courses(student_id)

            elif choice == '5':
                filename = input("Enter filename to save course catalog: ")
                self.save_course_catalog(filename)

            elif choice == '6':
                filename = input("Enter filename to load course catalog: ")
                self.load_course_catalog(filename)

            elif choice == '7':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice, please try again.")


if _name_ == "_main_":
    catalog_system = Catalog()
    catalog_system.menu()