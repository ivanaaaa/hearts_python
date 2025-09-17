import math
import time
import os

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create heart points
points = []
for y in range(15, -15, -1):
    row = ""
    for x in range(-30, 30):
        eq = ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3
        if eq <= 0:
            row += "*"
        else:
            row += " "
    points.append(row)

# Animate line by line
for i in range(len(points)):
    clear()
    for j in range(i+1):
        print(points[j])
    time.sleep(0.1)

print("\nDone! ❤️")
