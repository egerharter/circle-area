# Erik Gerharter
# 2018-11-16

# calculate the area of a circle

print("Let's calculate the area of a circle!")
radius = input("What is the radius of the circle (in meters)? ")

# give error message and get new input if user input is negative or not a number
while radius.replace(".", "", 1).isdigit() == False:
    radius = input("Sorry, \"" + radius + "\" is invalid. Enter a new value: ")

area = 3.14159 * (float(radius) ** 2)
print("Area =", area, "m^2")