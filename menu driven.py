#7.	Write a menu driven python program which perform the following:
# ●	Find area of circle 
# ●	Find area of triangle
# ●	Find area of square 
# ●	Find area of rectangle 
# Hint: Use infinite while loop for Menu

print("Menu:")
print("1. Find area of circle")
print("2. Find area of triangle")
print("3. Find area of square")
print("4. Find area of rectangle")
print("5. Exit")

while True:
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area_circle = 3.14 * radius * radius
        print(f"Area of the circle: {area_circle}")

    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area_triangle = 0.5 * base * height
        print(f"Area of the triangle: {area_triangle}")

    elif choice == 3:
        side = float(input("Enter the side of the square: "))
        area_square = side * side
        print(f"Area of the square: {area_square}")

    elif choice == 4:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area_rectangle = length * width
        print(f"Area of the rectangle: {area_rectangle}")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
        