# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P7
# Date: December 1, 2026
# p7_classes.py - a simple school system using classes and objects


class Subject:
    """A subject with a code, title, and number of units."""

    def __init__(self, code, title, units):
        self.code = code
        self.title = title
        self.units = units

    def display(self):
        print(f"  {self.code} - {self.title} ({self.units} units)")


class Student:
    """A student with a private grade that can only be changed safely."""

    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = 0              # private attribute (two underscores)
        self.set_grade(grade)         # validate the starting grade

    # Getter: the only way to read the private grade from outside
    def get_grade(self):
        return self.__grade

    # Setter: changes the grade only if it is valid
    def set_grade(self, new_grade):
        if isinstance(new_grade, (int, float)) and 0 <= new_grade <= 100:
            self.__grade = new_grade
            return True
        print(f"  Invalid grade '{new_grade}' for {self.name}. Grade must be 0-100.")
        return False

    def get_status(self):
        return "Passed" if self.__grade >= 75 else "Failed"

    def update_info(self, name=None, course=None):
        """Change the name and/or course. Leave a value as None to keep it."""
        if name:
            self.name = name
        if course:
            self.course = course

    def display(self):
        print(f"  {self.student_id:<10}{self.name:<22}{self.course:<12}"
              f"{self.__grade:>6.1f}  {self.get_status()}")


class Section:
    """A section that holds several Student objects and one Subject."""

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject        # a Subject object
        self.students = []            # a list of Student objects

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_class_average(self):
        if not self.students:
            return 0
        total = sum(student.get_grade() for student in self.students)
        return total / len(self.students)

    def list_students(self):
        print(f"\nSection: {self.name}")
        self.subject.display()
        print(f"\n  {'ID':<10}{'Name':<22}{'Course':<12}{'Grade':>6}  Status")
        print("  " + "-" * 58)
        for student in self.students:
            student.display()
        print(f"\n  Total students: {len(self.students)}")
        print(f"  Class average: {self.get_class_average():.2f}")