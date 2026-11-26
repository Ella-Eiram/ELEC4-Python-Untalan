# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P5
# Date: November 30, 2026
# p5_file_system.py - keeps student records in a text file (students.txt)

import os

# Save students.txt next to this script, even when run from the repo root
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")
SEPARATOR = "|"


def load_students():
    """Read all records from the file. Return an empty list if the file is missing."""
    students = []
    try:
        with open(FILE_PATH, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip blank lines
                student_id, name, section, average = line.split(SEPARATOR)
                students.append({
                    "id": student_id,
                    "name": name,
                    "section": section,
                    "average": float(average),
                })
    except FileNotFoundError:
        print("No students.txt yet - starting with an empty list.")
    return students


def save_students(students):
    """Write every record back to the file, one student per line."""
    with open(FILE_PATH, "w") as file:
        for s in students:
            file.write(f"{s['id']}{SEPARATOR}{s['name']}{SEPARATOR}"
                       f"{s['section']}{SEPARATOR}{s['average']}\n")


def find_student(students, student_id):
    """Return the student with this ID, or None if not found."""
    for s in students:
        if s["id"].lower() == student_id.lower():
            return s
    return None


def get_average():
    """Ask for a general average until a valid number from 0 to 100 is typed."""
    while True:
        try:
            average = float(input("General average (0-100): "))
            if 0 <= average <= 100:
                return average
            print("Average must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a number, not letters.")


def get_text(prompt):
    """Ask for text that is not empty and has no '|' (it would break the file)."""
    while True:
        text = input(prompt).strip()
        if not text:
            print("This field cannot be empty.")
        elif SEPARATOR in text:
            print(f'Please do not use the "{SEPARATOR}" character.')
        else:
            return text


def add_student(students):
    student_id = get_text("Student ID: ")
    if find_student(students, student_id):
        print(f"A student with ID {student_id} already exists.")
        return
    name = get_text("Full name: ")
    section = get_text("Course/Section: ")
    average = get_average()
    students.append({"id": student_id, "name": name,
                     "section": section, "average": average})
    save_students(students)
    print(f"{name} was saved to students.txt.")


def display_students(students):
    if not students:
        print("No records yet.")
        return
    print(f"\n{'ID':<12}{'Name':<25}{'Section':<15}{'Average':>8}")
    print("-" * 60)
    for s in students:
        print(f"{s['id']:<12}{s['name']:<25}{s['section']:<15}{s['average']:>8.2f}")
    print(f"Total records: {len(students)}")


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    s = find_student(students, student_id)
    if s:
        print(f"\nID: {s['id']}\nName: {s['name']}\n"
              f"Section: {s['section']}\nAverage: {s['average']:.2f}")
    else:
        print(f"No student found with ID {student_id}.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    s = find_student(students, student_id)
    if not s:
        print(f"No student found with ID {student_id}.")
        return
    print("Press Enter to keep the current value.")
    new_name = input(f"Full name [{s['name']}]: ").strip()
    new_section = input(f"Course/Section [{s['section']}]: ").strip()
    if new_name and SEPARATOR not in new_name:
        s["name"] = new_name
    if new_section and SEPARATOR not in new_section:
        s["section"] = new_section
    if input("Update average? (y/n): ").strip().lower() == "y":
        s["average"] = get_average()
    save_students(students)
    print("Record updated and saved.")


def main():
    print("Student Information File System - by Rhuella Marie Untalan")
    students = load_students()
    print(f"Loaded {len(students)} record(s).")

    while True:
        print("\n1. Add student")
        print("2. Display all students")
        print("3. Search by ID")
        print("4. Update student")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1-5.")


if __name__ == "__main__":
    main()