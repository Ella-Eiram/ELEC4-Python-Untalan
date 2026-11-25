# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P2
# Date: November 26, 2026
# student_utils.py - reusable functions for working with student grades

def compute_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def evaluate_passing_status(average):
    """Return 'Passed' if the average is 75 or higher, else 'Failed'."""
    if average >= 75:
        return "Passed"
    return "Failed"


def get_highest(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest(grades):
    """Return the lowest grade."""
    return min(grades)


# This block only runs when the file is run directly (python3 student_utils.py),
# NOT when another program imports it.
if __name__ == "__main__":
    sample = [80, 90, 70]
    print("Testing student_utils with", sample)
    print("Average:", compute_average(sample))
    print("Status:", evaluate_passing_status(compute_average(sample)))