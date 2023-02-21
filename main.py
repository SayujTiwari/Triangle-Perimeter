import math

# Function to calculate distance between two points
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ask user to enter the coordinates of the three vertices of a triangle
x1 = input("Enter the x coordinates of vertex 1: ")
y1 = input("Enter the y coordinates of vertex 1: ")

x2 = input("Enter the x coordinates of vertex 2: ")
y2 = input("Enter the y coordinates of vertex 2: ")

x3 = input("Enter the x coordinates of vertex 3: ")
y3 = input("Enter the y coordinates of vertex 3: ")

# Convert input to float
x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)

# Calculate the side lengths of the triangle
a = dist(x1, y1, x2, y2)
b = dist(x2, y2, x3, y3)
c = dist(x1, y1, x3, y3)

# Calculate the perimeter of the triangle
perimeter = a + b + c

# Output the side lengths and perimeter of the triangle
print("Side a: ", a)
print("Side b: ", b)
print("Side c: ", c)
print("Perimeter: ", perimeter)