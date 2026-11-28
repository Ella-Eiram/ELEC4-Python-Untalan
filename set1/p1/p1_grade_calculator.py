# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P1
# Date: November 18, 2026
# p1_grade_calculator.py - menu-driven grade calculator built from functions


def compute_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def get_highest(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest(grades):
    """Return the lowest grade."""
    return min(grades)


def evaluate_passing_status(grades):
    """Return 'Passed' if the average is 75 or higher, else 'Failed'."""
    if compute_average(grades) >= 75:
        return "Passed"
    return "Failed"


def get_valid_grade():
    """Keep asking until the user types a number from 0 to 100."""
    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be 0 to 100.")
        except ValueError:
            print("Please type a number.")


def enter_grades():
    """Ask how many grades, then collect each one. Returns a list of grades."""
    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
            print("Please enter at least 1.")
        except ValueError:
            print("Please type a whole number.")

    new_grades = []
    for i in range(count):
        new_grades.append(get_valid_grade())
    return new_grades


print("Grade Calculator by Rhuella Marie Untalan")
grades = []   # global: used by the menu the whole time the program runs

while True:
    print("\n1. Enter grades")
    print("2. View results")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        grades = enter_grades()

    elif choice == "2":
        # tell the user to enter grades first if the list is empty
        if not grades:
            print("No grades entered yet.")
        else:
            print(f"Average: {compute_average(grades):.2f}")
            print(f"Highest: {get_highest(grades)}")
            print(f"Lowest: {get_lowest(grades)}")
            print(f"Status: {evaluate_passing_status(grades)}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please pick 1, 2, or 3.")


# LOCAL vs GLOBAL VARIABLES:
# A global variable is created outside any function, like my grades list,
# so the menu can use it for the whole time the program is running.
# A local variable is created inside a function and only exists while that
# function runs, like count and new_grades inside enter_grades().
# The grades parameter in compute_average(grades) is also local, even though
# it has the same name as the global list.
# If I tried to print new_grades outside enter_grades(), Python would give a
# NameError because that variable no longer exists there.