year=int(input("Enter leap year"))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")

cm=int(input("Enter the height in centimeters:"))
print(cm)
Inches = cm*0.394
Feet = cm*0.0328
print(("The length in inches",round(Inches,2)))
print(("The length in feet",round(Feet,2)))


