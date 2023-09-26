# This program asks the user for their name and then prints it back to them.

name = input("What is your name? ")
print("Hello, {}!".format(name))

# This program calculates the area of a circle.

radius = float(input("What is the radius of the circle? "))
area = 3.14 * radius ** 2
print("The area of the circle is {}.".format(area))

# This program calculates the volume of a cube.

length = float(input("What is the length of the cube? "))
width = float(input("What is the width of the cube? "))
height = float(input("What is the height of the cube? "))
volume = length * width * height
print("The volume of the cube is {}.".format(volume,))