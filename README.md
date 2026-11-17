# Average of Three Marks — Python Homework 1

## 1. Project overview

This beginner-friendly Python program asks the user to enter three marks, calculates their average using a **function**, and displays the result.

The assignment is from **Cybersecurity Programming — Homework 1**, First Semester 2026/2027, Aqaba University of Technology.

## 2. Requirements

- Python 3
- A terminal or Python editor (for example, IDLE or VS Code)

No external libraries are required. The program uses Python's built-in `input()`, `float()`, and `print()` features.

## 3. How to run the program

1. Make sure Python 3 is installed.
2. Open a terminal in the folder containing `HW1_Average_Three_Marks.py`.
3. Run:

   ```bash
   python HW1_Average_Three_Marks.py
   ```

4. Enter the first, second, and third marks when prompted.
5. Read the calculated average displayed on the screen.

## 4. Example

```text
Enter the first mark: 80
Enter the second mark: 90
Enter the third mark: 70
The average of the three marks is: 80.00
```

The calculation is:

\[
\text{Average} = \frac{80 + 90 + 70}{3} = 80
\]

## 5. Code explanation — every line

The explanations below follow the exact line numbers in `HW1_Average_Three_Marks.py`.

| Line | Code | What the line does |
|---:|---|---|
| 1 | `# Name: Loai Mustafa El-Afify` | A comment that identifies the student. Python ignores comments when it runs the program. |
| 2 | `# Cybersecurity Programming - Homework 1` | A comment that identifies the course and assignment. |
| 3 | *(blank line)* | Separates the header comments from the function to make the code easier to read. |
| 4 | `# This function calculates and returns the average of three marks.` | A comment describing the purpose of the function below it. |
| 5 | `def calculate_average(mark1, mark2, mark3):` | Defines a function named `calculate_average`. It receives three values as parameters. The colon starts the function body. |
| 6 | `    total = mark1 + mark2 + mark3` | Adds the three marks and stores their sum in the variable `total`. |
| 7 | `    average = total / 3` | Divides the sum by `3` and stores the result in `average`. |
| 8 | `    return average` | Sends the calculated average back to the part of the program that called the function. |
| 9 | *(blank line)* | Separates the function from the input section. |
| 10 | `# Ask the user to enter three marks and handle non-numeric input.` | A comment explaining that the next section gets the marks and handles invalid numeric input. |
| 11 | `try:` | Starts a `try` block. Python runs the indented statements and checks whether they produce the handled error. |
| 12 | `    mark1 = float(input("Enter the first mark: "))` | Displays a prompt, reads the first mark, converts the entered text to a number, and stores it in `mark1`. |
| 13 | `    mark2 = float(input("Enter the second mark: "))` | Reads and converts the second mark, then stores it in `mark2`. |
| 14 | `    mark3 = float(input("Enter the third mark: "))` | Reads and converts the third mark, then stores it in `mark3`. |
| 15 | *(blank line)* | Separates the input statements from the calculation and output. |
| 16 | `    result = calculate_average(mark1, mark2, mark3)` | Calls the function with the three marks and stores the returned average in `result`. |
| 17 | `    print(f"The average of the three marks is: {result:.2f}")` | Displays the result. The `f` lets Python insert the value of `result`; `.2f` displays it to two digits after the decimal point. |
| 18 | `except ValueError:` | Starts an error-handling block. It runs if converting an entered value with `float()` fails, such as when the user types `hello`. |
| 19 | `    print("Invalid input. Please enter numeric marks only.")` | Displays a helpful message when one or more entries are not numeric. |

## 6. Main function logic

The key function is:

```python
def calculate_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return average
```

It follows three steps:

1. Receive the three marks.
2. Add them together and divide the total by three.
3. Return the average to the main program.

The function is reusable: another part of a program could call `calculate_average(80, 90, 70)` without asking the user for input again.

## 7. Input and calculation notes

- The program accepts whole-number marks (such as `85`) and decimal marks (such as `85.5`).
- The program checks that entries can be converted to numbers.
- The assignment sheet does not specify a minimum or maximum mark, so this solution does not impose a mark range.
- The average is calculated using the full numeric values. Only the displayed result is formatted to two decimal places.

## 8. Files

- `HW1_Average_Three_Marks.py` — the Python source code requested by the assignment.
- `README.md` — project overview, run instructions, example, and explanation of every source-code line.
