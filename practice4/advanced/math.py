# Interactive math operations
import math


def degree_to_radian(degree):
    return math.radians(degree)


def trapezoid_area(height, base1, base2):
    return (base1 + base2) / 2 * height


def regular_polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))


def parallelogram_area(base, height):
    return base * height


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
        elif choice == "2":
            height = float(input("Height: "))
            base1 = float(input("Base 1: "))
            base2 = float(input("Base 2: "))
            print("Expected Output:", trapezoid_area(height, base1, base2))
        elif choice == "3":
            num_sides = int(input("Number of sides: "))
            side_length = float(input("Length of a side: "))
            print("The area of the polygon is:", round(regular_polygon_area(num_sides, side_length), 2))
        elif choice == "4":
            base = float(input("Length of base: "))
            height = float(input("Height of parallelogram: "))
            print("Expected Output:", parallelogram_area(base, height))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
