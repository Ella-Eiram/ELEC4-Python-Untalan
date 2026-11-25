# Name: Rhuella Marie Untalan
# Section: IV-BSIT _
# Activity: P4
# Date: November 26, 2026
# p4_exceptions.py - menu-driven program that handles bad input without crashing

import os

# Folder where this script is saved, so file names are found even when
# the program is run from the repository root
SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def divide_numbers():
    """Ask for two numbers and divide them, handling bad input."""
    try:
        dividend = float(input("Enter the first number: "))
        divisor = float(input("Enter the second number: "))
        result = dividend / divisor
    except ValueError:
        print("Error: Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    else:
        # Runs only if no exception happened
        print(f"Result: {dividend} / {divisor} = {result:.2f}")
    finally:
        # Always runs, error or not
        print("Division attempt finished.")


def open_file():
    """Ask for a file name and display its contents."""
    filename = input("Enter the file name: ").strip()
    file_path = os.path.join(SCRIPT_FOLDER, filename)
    try:
        with open(file_path, "r") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f'Error: The file "{filename}" does not exist.')
    except IsADirectoryError:
        # Happens when the name is a folder, or when nothing is typed
        print(f'Error: "{filename}" is a folder, not a file.')
    else:
        print(f"\n----- {filename} -----")
        print(contents)
    finally:
        print("File operation finished.")


def get_menu_choice():
    """Return the menu choice as a number, or None if it is invalid."""
    try:
        choice = int(input("Choose: "))
    except ValueError:
        return None
    if choice not in (1, 2, 3):
        return None
    return choice


def main():
    print("Safe Menu Program - by Rhuella Marie Untalan")
    while True:
        print("\n1. Divide two numbers")
        print("2. Open a file")
        print("3. Exit")
        choice = get_menu_choice()

        if choice == 1:
            divide_numbers()
        elif choice == 2:
            open_file()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl + C closes the program cleanly instead of showing an error
        print("\nProgram stopped by the user.")