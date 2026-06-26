# This file contains interactive math exercises.
import math


# This function converts degrees to radians.
def degree_to_radian(degree):
    return math.radians(degree)


# This function calculates the area of a trapezoid.
def trapezoid_area(height, base1, base2):
    return (base1 + base2) / 2 * height


# This function calculates the area of a regular polygon.
def regular_polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))


# This function calculates the area of a parallelogram.
def parallelogram_area(base, height):
    return base * height


# This function runs the interactive menu for the math exercises.
def main():
    while True:
        print("\nMath Menu")
        print("1. Convert degree to radian")
        print("2. Area of a trapezoid")
        print("3. Area of a regular polygon")
        print("4. Area of a parallelogram")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            degree = float(input("Enter degree: "))
            print("Output radian:", round(degree_to_radian(degree), 6))
            # Example output for 15 degrees: 0.261799
        elif choice == "2":
            height = float(input("Height: "))
            base1 = float(input("Base 1: "))
            base2 = float(input("Base 2: "))
            print("Expected Output:", trapezoid_area(height, base1, base2))
            # Example output for 5, 5, 6: 27.5
        elif choice == "3":
            num_sides = int(input("Number of sides: "))
            side_length = float(input("Length of a side: "))
            print("The area of the polygon is:", round(regular_polygon_area(num_sides, side_length), 2))
            # Example output for 4 sides and 25 length: 625.0
        elif choice == "4":
            base = float(input("Length of base: "))
            height = float(input("Height of parallelogram: "))
            print("Expected Output:", parallelogram_area(base, height))
            # Example output for base 5 and height 6: 30.0
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
