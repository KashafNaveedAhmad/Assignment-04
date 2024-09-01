# Hello, from Kashaf naveed ahmad's side.
# Let's create some functions.

import math
import time

# Assignment-04
print("\n-->Let's start the assignment!!")

# Calculate your age based on the current year and your birth year.

def age(birth_year)->int:
    
    current_year=int(time.strftime('%Y'))
    age_calculate=current_year-birth_year
    return age_calculate

# Write a program that calculates the area of a rectangle using length and width variables.
def area_of_rectangle(length:float,width:float):
    area=length*width
    return area


# Area of a circle (Formula:(math.pi)*(radius**2))
def area_of_circle(radius_of_circle):
    area_of_circle_calculate=((math.pi)*(radius_of_circle**2))
    return area_of_circle_calculate


# Write a program that calculates the area of the cube.

def area_of_cube(side_of_cube):    
    area_of_cube_calculate=(6*(side_of_cube**2))
    return area_of_cube_calculate

    
#Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
def F_to_C(input_fahrenheit):
    celsius=float((5/9)*(input_fahrenheit-32))
    return celsius

# Celsius to Fahrenheit (Formula:((9/5)*C)+32))
def C_to_F(input_celsius):    
    fahrenheit=(((9/5)*input_celsius)+32)
    return fahrenheit


# Convert a given number of seconds into minutes and minutes into seconds using variables.

def sec_to_min(sec):
    min=float(sec/60)
    return min
# Minutes into Seconds (Formula:minutes*60)
def min_to_sec(min):
    sec=float(min*60)
    return sec

# Write a program that calculates the percentage.
# Percentge calculation
def percentage(num1,num2):
    percentage_calculate=(num1/num2)*100
    return percentage_calculate
    

# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
def BMI(Bmi_height,Bmi_weight):
    BMI_result=Bmi_weight/Bmi_height**2
    return BMI_result
    

# Write a program that calculates the volume of a cylinder using the formula.

def area_of_cylinder(height_cylinder,radius_cylinder):
    cy1=2*math.pi*(radius_cylinder**2)
    cy2=2*math.pi*radius_cylinder*height_cylinder
    area_of_cylinder_calculate=cy1+cy2
    return area_of_cylinder_calculate


#OUTSIDE THE FUNCTIONS.  
# Age     
print("\nWe are going to calculate your age.\nBelow:")
birth_year=int(input("Enter your birth year:"))  
print("Your age based on your birth year is:",age(birth_year),"years old.")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")    


# Area of a recatangle(length*width)
print("\nLet's calculates the 'Area of a rectangle'.\nBelow:")
length=float(input("Enter the lenght:"))
width=float(input("Enter the width:"))
print("The area of rectangle is:",area_of_rectangle(length,width))  
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


# Write a program that calculates the area of a circle.
print("\nLet's calculate the 'Area of Circle'.\nBelow:")
radius_of_circle=float(input("Enter the radius:"))
print("The area of circle is:",area_of_circle(radius_of_circle))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# Area of a cube (Formula:6(a^2))
print("\nLet's calculate the 'Area of Cube'.\nBelow:")
side_of_cube=int(input("Enter the it's side:"))
print("The area of cube is:",area_of_cube(side_of_cube))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    
# Fahrenheit to Celsius (Formula:(5/9)*(F-32))
print("\nWe are going to convert 'Fahrenheit' into 'Celsius': \nBelow:")
input_fahrenheit=float(input("Enter the temperature in 'Fahrenheit':"))
print("The converted temperature in 'Celsius' is:",F_to_C(input_fahrenheit),"°C")
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# Celsius to Fahrenheit (Formula:((9/5)*C)+32))   
print("\nWe are going to convert 'Celsius' into 'Fahrenheit': \nBelow:")
input_celsius=float(input("Enter the temperature in 'Celsius':"))
print("The converted temperature in 'Fahrenheit' is:",C_to_F(input_celsius),"°F")  
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    
# Seconds into Minutes (Formula:seconds/60)
print("\nTo calculate number of seconds into minutes.\nEnter values below:")
sec=int(input("Enter the seconds to be converted into minutes:"))
print("Based on the seconds the minutes are :",sec_to_min(sec))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# Minutes into Seconds (Formula:minutes*60)

print("\nTo calculate number of minutes into seconds.\nEnter values below:")
min=float(input("Enter the minutes to be converted into seconds:"))
print("Based on the minutes the seconds are :",min_to_sec(min))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


# Percentge calculation

print("\nLet's calculate the percentage.\nBelow:")
num1=int(input("Enter the obtained number:"))
num2=int(input("Enter the total number:")) 
print("The percentage is:",percentage(num1,num2),'%')
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
# BMI using height (in meters) and weight (in kilograms) variables.(Formula:weight/height^2)
# BMI_Formula=weight/height^2
print("\nLet's calculate BMI (Body mass index).\nBelow:")
Bmi_height=float(input("Enter the height(m):"))
Bmi_weight=float(input("Enter the weight(Kg):"))
print("The calculated BMI is:",BMI(Bmi_height,Bmi_weight))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")



# Area of a cylinder (Formula:A=2π*(r^2)+2πrh)

print("\nWe are going to calculate the 'Area of Cylinder' :\nBelow:")
height_cylinder=float(input("Enter the height:"))
radius_cylinder=float(input("Enter the radius:"))
print("The area of cylinder is:",area_of_cylinder(height_cylinder,radius_cylinder))
print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

print("\n THANKYOU!")


