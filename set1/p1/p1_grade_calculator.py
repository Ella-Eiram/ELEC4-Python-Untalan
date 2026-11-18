# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P1
# Date: November 18, 2026

def compute_average(grades):
    return sum(grades) / len(grades)

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    # return the lowest grade (hint: min)
    return min(grades)

def evaluate_passing_status(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"



def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be 0 to 100.")
        except ValueError:
            print("Please type a number.")

print("Grade Calculator by Rhuella Marie Untalan")
grades = []

while True:
    print("\n1. Enter grades")
    print("2. View results")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        # ask how many grades, then get each one
        count = int(input("How many grades? "))
        for i in range(count):
            grade = get_valid_grade()
            grades.append(grade)

    elif choice == "2":
        # if grades is empty, tell the user to enter grades first
        if not grades:
            print("No grades entered yet.")
        else:
            # otherwise print the average, highest, lowest and status
            average = compute_average(grades)
            print(f"Average: {average:.2f}")
            print(f"Highest: {get_highest(grades)}")
            print(f"Lowest: {get_lowest(grades)}")
            print(f"Status: {evaluate_passing_status(average)}")
    
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
