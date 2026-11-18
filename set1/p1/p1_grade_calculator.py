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

    

grades = [80, 90, 70]
print(compute_average(grades))
print(get_highest(grades))
print(get_lowest(grades))
print(evaluate_passing_status(compute_average(grades)))


