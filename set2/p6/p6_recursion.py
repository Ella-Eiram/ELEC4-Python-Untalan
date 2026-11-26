# Name: Rhuella Marie Untalan
# Section: IV-BSIT A
# Activity: P6
# Date: November 30, 2026
# p6_recursion.py - four recursive functions with a menu to run them


# Base case: n is 0 or 1, return 1
# Recursive call: n * factorial(n - 1)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base case: n is 0 or 1, return n (fib(0) = 0, fib(1) = 1)
# Recursive call: fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: n is 0, return an empty list
# Recursive call: fibonacci_terms(n - 1) plus the next term
# (Builds the first n terms of the sequence without a loop)
def fibonacci_terms(n):
    if n == 0:
        return []
    return fibonacci_terms(n - 1) + [fibonacci(n - 1)]


# Base case: n is 0, return 0
# Recursive call: n + sum_numbers(n - 1)
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case 1: the list is empty, return False (target not found)
# Base case 2: the first item equals the target, return True
# Recursive call: search(items[1:], target) - search the rest of the list
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def get_whole_number(prompt, maximum):
    """Ask for a whole number from 0 to maximum."""
    while True:
        try:
            number = int(input(prompt))
            if 0 <= number <= maximum:
                return number
            print(f"Please enter a number from 0 to {maximum}.")
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("Recursion Toolkit - by Rhuella Marie Untalan")
    while True:
        print("\n1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of 1 to n")
        print("4. Search a list")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            n = get_whole_number("Enter n (0-100): ", 100)
            print(f"{n}! = {factorial(n)}")

        elif choice == "2":
            # Capped at 30 because this simple recursion slows down for big n
            n = get_whole_number("Enter n (0-30): ", 30)
            print(f"Fibonacci number #{n} = {fibonacci(n)}")
            print(f"First {n} terms: {fibonacci_terms(n)}")

        elif choice == "3":
            n = get_whole_number("Enter n (0-500): ", 500)
            print(f"Sum of 1 to {n} = {sum_numbers(n)}")

        elif choice == "4":
            raw = input("Enter items separated by commas (e.g. apple, mango, 5): ")
            items = [item.strip() for item in raw.split(",") if item.strip()]
            target = input("Enter the value to search for: ").strip()
            found = search(items, target)
            print(f"List: {items}")
            print(f'"{target}" found? {found}')

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1-5.")


if __name__ == "__main__":
    main()