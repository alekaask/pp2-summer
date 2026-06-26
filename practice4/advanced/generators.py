# Interactive generator exercises

def squares_up_to(n):
    for i in range(n + 1):
        yield i * i


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def squares(start, end):
    for i in range(start, end + 1):
        yield i * i


def countdown(n):
    while n >= 0:
        yield n
        n -= 1


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
        elif choice == "2":
            n = int(input("Enter n: "))
            print(", ".join(str(x) for x in even_numbers(n)))
        elif choice == "3":
            n = int(input("Enter n: "))
            print(list(divisible_by_3_and_4(n)))
        elif choice == "4":
            start = int(input("Enter a: "))
            end = int(input("Enter b: "))
            for value in squares(start, end):
                print(value)
        elif choice == "5":
            n = int(input("Enter n: "))
            print(list(countdown(n)))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
