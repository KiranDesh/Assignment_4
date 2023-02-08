#*) Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder. 
#Sample output:
#The area of the rectangle is *)6.*)m2
#The volume of the cylinder is *)4.*)cm3 =pi*(r**2)*h


def area_vol(width,length,radius,height):
    area_rect = width*length
    vol_cyl = 3.14*(radius**2)*height
    print("The area of the rectangle is{0} m\u00b2".format(area_rect))
    print("The volume of the cylinder is {0:0.2f} cm\u00b3".format(vol_cyl))
    
width = int(input("Enter a width for rectangle  : "))
length = int(input("Enter a length for rectangle : "))
radius = int(input("Enter a radius for volume of cylinder : "))
height = int(input("Enter a height for volume of cylinder : "))

area_vol(width,length,radius,height)