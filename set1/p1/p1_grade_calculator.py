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

print(get_valid_grade())
