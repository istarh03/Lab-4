"""
Program Name: Lab15_Istar-2.py
Author: Istar Hagi
Purpose: Plot cubic numbers. Part 1 plots the first 5 cubes using
         lists typed by hand. Part 2 plots the first 5000 cubes using
         lists generated automatically. Each plot is saved as a PNG file.
Starter Code: No starter code was used. This program is based on
              "Try It Yourself 15-1" from Python Crash Course.
Date: November 23, 2026
"""

import matplotlib.pyplot as plt

# ----- Part 1: First 5 Cubes -----
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values)
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.savefig("cubes_5.png")
plt.close()


# ----- Part 2: First 5000 Cubes -----
x_values = list(range(1, 5001))

y_values = []
for number in x_values:
    y_values.append(number ** 3)

plt.plot(x_values, y_values)
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.savefig("cubes_5000.png")
plt.close()