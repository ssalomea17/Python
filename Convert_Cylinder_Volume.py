'''(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * '''

radius = eval(input("Enter radius "))
length = eval(input("and length "))
pi = 3.14
area = radius * radius * pi
volume = area * length
print("The area is" , area)
print("The volume is" , volume)