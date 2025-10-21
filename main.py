# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

PREVIOUS_NUMBER = 0
SUM_OF_NUMBERS = 0

for i in range(10):
    SUM_OF_NUMBERS = i + PREVIOUS_NUMBER
    print(
        f"Current Number {i} Previous Number {PREVIOUS_NUMBER} Sum: {SUM_OF_NUMBERS}")
    PREVIOUS_NUMBER = i
