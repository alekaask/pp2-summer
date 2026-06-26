# This file contains interactive generator exercises.

# This generator yields the squares of numbers from 0 to n.
def squares_up_to(n):
    for i in range(n + 1):
        yield i * i


# This generator yields even numbers from 0 to n.
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# This generator yields numbers that are divisible by both 3 and 4.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# This generator yields squares for every number between start and end.
def squares(start, end):
    for i in range(start, end + 1):
        yield i * i


# This generator yields numbers from n down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# This function runs the interactive menu for the generator examples.
def main():
    while True:
        print("\nGenerator Menu")
        print("1. Squares up to N")
        print("2. Even numbers from 0 to n")
        print("3. Numbers divisible by 3 and 4")
        print("4. Squares from a to b")
        print("5. Numbers from n down to 0")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Enter N: "))
            print(list(squares_up_to(n)))
            # Example output for n = 5: [0, 1, 4, 9, 16, 25]
        elif choice == "2":
            n = int(input("Enter n: "))
            print(", ".join(str(x) for x in even_numbers(n)))
            # Example output for n = 10: 0, 2, 4, 6, 8, 10
        elif choice == "3":
            n = int(input("Enter n: "))
            print(list(divisible_by_3_and_4(n)))
            # Example output for n = 24: [0, 12, 24]
        elif choice == "4":
            start = int(input("Enter a: "))
            end = int(input("Enter b: "))
            for value in squares(start, end):
                print(value)
            # Example output for a = 3 and b = 6: 9, 16, 25, 36
        elif choice == "5":
            n = int(input("Enter n: "))
            print(list(countdown(n)))
            # Example output for n = 5: [5, 4, 3, 2, 1, 0]
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
