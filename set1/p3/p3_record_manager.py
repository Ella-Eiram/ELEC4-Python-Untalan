# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P3
# Date: November 26, 2026
# p3_record_manager.py - menu-driven program that manages student names

students = []         # list: keeps each name as the user typed it
name_keys = set()     # set: lowercase versions, used for fast duplicate checks


def add_student(name):
    """Add a name unless it already exists (case-insensitive)."""
    key = name.lower()
    if key in name_keys:
        print(f'"{name}" is already in the records.')
        return
    students.append(name)
    name_keys.add(key)
    print(f'"{name}" added.')


def remove_student(name):
    """Remove a name if it exists (case-insensitive)."""
    key = name.lower()
    if key not in name_keys:
        print(f'"{name}" was not found.')
        return
    for student in students:
        if student.lower() == key:
            students.remove(student)
            break
    name_keys.remove(key)
    print(f'"{name}" removed.')


def search_student(keyword):
    """Show every name that contains the keyword (partial, case-insensitive)."""
    matches = [s for s in students if keyword.lower() in s.lower()]
    if matches:
        print(f"Found {len(matches)} match(es):")
        for name in sorted(matches, key=str.lower):
            print(f"  - {name}")
    else:
        print(f'No student matches "{keyword}".')


def display_students():
    """Show all names alphabetically, numbered, with the total count."""
    if not students:
        print("No students recorded yet.")
        return
    print("\n----- STUDENT LIST -----")
    for number, name in enumerate(sorted(students, key=str.lower), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def main():
    print("Student Record Manager - by Rhuella Marie Untalan")
    while True:
        print("\n1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                add_student(name)
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            remove_student(input("Enter name to remove: ").strip())
        elif choice == "3":
            search_student(input("Enter name or part of a name: ").strip())
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1-5.")


if __name__ == "__main__":
    main()


# LIST vs SET (write this part in your own words):
# A list keeps items in order, allows duplicates, and lets you access items by
# position. A set has no order, never keeps duplicates, and checks membership
# very quickly. In this program I used a list (students) to store the names as
# they were typed so I could sort and number them for display. I used a set
# (name_keys) to store lowercase copies so I could quickly check whether a
# name like "juan cruz" already exists as "Juan Cruz".