# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P8
# Date: December 1, 2026
# p8_inheritance.py - parent and child classes showing inheritance and polymorphism


class Person:
    """Parent class: attributes and a method every person has."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")


class Student(Person):
    """Child class: a Person who also has a course and year level."""

    def __init__(self, name, age, course, year_level):
        super().__init__(name, age)       # let Person set name and age
        self.course = course
        self.year_level = year_level

    # Overrides Person.introduce()
    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.year_level} {self.course} student "
              f"and I'm {self.age} years old.")


class Teacher(Person):
    """Child class: a Person who also teaches a subject."""

    def __init__(self, name, age, subject, years_teaching):
        super().__init__(name, age)
        self.subject = subject
        self.years_teaching = years_teaching

    # Overrides Person.introduce()
    def introduce(self):
        print(f"Good day! I'm {self.name}, and I teach {self.subject}. "
              f"I've been teaching for {self.years_teaching} years.")


class Staff(Person):
    """Child class: a Person who works in a school office."""

    def __init__(self, name, age, office):
        super().__init__(name, age)
        self.office = office

    # Overrides Person.introduce(), but also reuses the parent's version
    def introduce(self):
        super().introduce()
        print(f"   I work at the {self.office}.")



def main():
    print("Inheritance and Polymorphism - by Rhuella Marie Untalan\n")

    # Objects of different classes, all stored in one list
    people = [
        Person("Pedro Penduko", 30),
        Student("Rhuella Marie Untalan", 21, "BSIT", "4th year"),
        Teacher("Mr. Santos", 40, "Python Programming", 10),
        Student("Juan Dela Cruz", 22, "BSIT", "4th year"),
        Staff("Ms. Reyes", 35, "Registrar's Office"),
    ]

    # Polymorphism: the same call, introduce(), gives a different
    # output depending on each object's class
    for person in people:
        print(f"[{type(person).__name__}]")
        person.introduce()
        print()

    # Inheritance check: every child object is also a Person
    print("Is each object a Person?")
    for person in people:
        print(f"  {person.name}: {isinstance(person, Person)}")


if __name__ == "__main__":
    main()


# INHERITANCE AND POLYMORPHISM (write this in your own words, 3-5 sentences):
#