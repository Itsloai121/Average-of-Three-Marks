# Name: Loai Mustafa El-Afify
# Cybersecurity Programming - Homework 1

# This function calculates and returns the average of three marks.
def calculate_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return average

# Ask the user to enter three marks and handle non-numeric input.
try:
    mark1 = float(input("Enter the first mark: "))
    mark2 = float(input("Enter the second mark: "))
    mark3 = float(input("Enter the third mark: "))

    result = calculate_average(mark1, mark2, mark3)
    print(f"The average of the three marks is: {result:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric marks only.")
