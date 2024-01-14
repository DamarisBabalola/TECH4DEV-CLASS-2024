# -*- coding: utf-8 -*-
"""Exercise_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1atw6-GsjFWQzV4hNb6fm17yM9K8Wt00i
"""



import pandas as pd
import numpy as np

"""1. write a Python program to produce the following output using for loop:
+----+\
\     /\
/    \\\
\    /\
/    \\\
\    /\
/    \\\
+----+
"""

def draw_box():
    print("+----+")
    for i in range(4):
        print("\\    /")
        print("/    \\")

    print("+----+")

# Call the function to draw the box
draw_box()

"""2. write a program to produce the following output using for loop:"""

def draw_pattern(rows, cols):
    for _ in range(rows):
        print('*' * cols)

# Call the function to draw the pattern
draw_pattern(5, 10)

"""### 3."""

for num in range(1, 7):
    print(num)

for i in range(1, 7):
    print(i * 2)

for i in range(1, 7):
    result = 15 * i - 11
    print(result)

for i in range(1, 7):
    result = 30 - 10 * (i - 1)
    print(result)

for i in range(1, 7):
    # Calculate the corresponding number based on the pattern
    number = i * 4 - 11

    # Print the calculated number
    print(number)

for i in range(1, 7):
    print(97 - 3 * (i - 1))

for i in range(1, 7):
    result = -4 + 18 * (i - 1)
    print(result)

"""### 4."""

class NumberTriangle:
    # Class constant to define the number of lines in the figure
    NUM_LINES = 8

    def draw_triangle(self):
        for i in range(1, self.NUM_LINES + 1):
            for j in range(i):
                print(i, end="")
            print()  # Move to the next line after each inner loop

# Create an instance of the class and call the method to draw the triangle
triangle = NumberTriangle()
triangle.draw_triangle()

"""### 5."""

def pay(hourly_rate, hours_worked):
    regular_hours = 8
    overtime_rate = 1.5 * hourly_rate

    if hours_worked <= regular_hours:
        total_pay = hourly_rate * hours_worked
    else:
        regular_pay = hourly_rate * regular_hours
        overtime_pay = overtime_rate * (hours_worked - regular_hours)
        total_pay = regular_pay + overtime_pay

    return total_pay

# Example usage:
salary = pay(5.50, 6)
print(f"Salary for 6 hours: ${salary:.2f}")

salary_overtime = pay(4.00, 11)
print(f"Salary for 11 hours: ${salary_overtime:.2f}")

"""### 6."""

import math

def circle_area(radius):
    return math.pi * radius ** 2

# Example usage:
radius = 2.0
result = circle_area(radius)
print(f"The area of a circle with radius {radius} is: {result}")

"""### 7."""

low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)

"""### 8."""

# Initialize sum to 0
sum = 0

# Prompt the user for numbers until 0 is entered
while True:
    num = int(input("Enter a number (type 0 to exit): "))

    # Break the loop if the user enters 0
    if num == 0:
        break

    # Add the entered number to the sum
    sum += num

# Output the sum
print("Sum of the entered numbers:", sum)

"""### 9."""

# Initialize sum to 0
sum = 0

# Prompt the user for numbers until -1 is entered
while True:
    num = int(input("Enter a number (type -1 to exit): "))

    # Break the loop if the user enters -1
    if num == -1:
        break

    # Add the entered number to the sum
    sum += num

# Output the sum
print("Sum of the entered numbers:", sum)

"""### 10"""

def repl(input_string, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return input_string * repetitions

# Example usage:
result = repl("hello", 3)
print(result)

"""### 11"""

def printRange(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i, end=" ")
    elif start > end:
        for i in range(start, end - 1, -1):
            print(i, end=" ")
    else:
        print(start)

# Example usage:
printRange(2, 7)
print()  # New line for separation
printRange(19, 11)
print()  # New line for separation
printRange(5, 5)

"""### 12."""

def smallestLargest():
    count = int(input("How many numbers do you want to enter? "))

    if count <= 0:
        print("Please enter a valid number greater than 0.")
        return

    smallest = float('inf')  # Initialize smallest to positive infinity
    largest = float('-inf')  # Initialize largest to negative infinity

    for i in range(1, count + 1):
        num = float(input(f"Number {i}: "))
        smallest = min(smallest, num)
        largest = max(largest, num)

    print(f"Smallest = {smallest}")
    print(f"Largest = {largest}")

# Call the function to execute the program
smallestLargest()

"""### 13."""

def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Type a number: "))

        if num < 0:
            break

        total += num
        count += 1

    if count > 0:
        average = total / count
        print(f"Average was {average:.1f}")
    else:
        print("No nonnegative numbers entered.")

# Call the function to execute the program
printAverage()

"""### 14."""

def numUnique(num1, num2, num3):
    unique_numbers = set([num1, num2, num3])
    return len(unique_numbers)


numUnique(5,7,5)

"""### 15."""

import random

def roll_dice():
    return random.randrange(1, 7)

def simulate_game():
    target_sum = 7
    tries = 0

    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()

        print(f"{dice1} + {dice2} = {dice1 + dice2}")

        tries += 1

        if dice1 + dice2 == target_sum:
            print(f"You won after {tries} tries!")
            break

# Call the function to simulate the game
simulate_game()

simulate_game()
