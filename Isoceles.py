side1 = float(input("Enter one of the sides of the triangle: "))
side2 = float(input("Enter another of the sides of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if (side1 == side2 and side3 != side1) or (side2 == side3 and side1 != side2) or (side3 == side1 and side2 != side1):
    print("That is an isoceles triangle. ")
else:
    print("That triangle is not isoceles. ")