# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P2
# Date: November 26, 2026
# p2_main.py - generates a grade report using the student_utils module

import student_utils                                  # Import style 1: import module
from student_utils import get_highest, get_lowest    # Import style 2: from module import name
from datetime import datetime                         # Built-in module


def get_valid_grade():
    """Keep asking until the user types a number from 0 to 100."""
    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    print("Student Grade Report - by Rhuella Marie Untalan\n")

    count = int(input("How many grades? "))
    grades = [get_valid_grade() for _ in range(count)]

    # Style 1: call through the module name
    average = student_utils.compute_average(grades)
    status = student_utils.evaluate_passing_status(average)

    # Style 2: call the imported names directly
    highest = get_highest(grades)
    lowest = get_lowest(grades)

    print("\n----- GRADE REPORT -----")
    print(f"Grades:  {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest:  {lowest}")
    print(f"Status:  {status}")
    print(f"Generated on: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")


if __name__ == "__main__":
    main()