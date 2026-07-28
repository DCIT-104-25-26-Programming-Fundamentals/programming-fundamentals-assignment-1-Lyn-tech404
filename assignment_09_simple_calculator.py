def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def main():
    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))

            if choice == "1":
                result = add(first, second)
                print("Result:", first, "+", second, "=", result)

            elif choice == "2":
                result = subtract(first, second)
                print("Result:", first, "-", second, "=", result)

            elif choice == "3":
                result = multiply(first, second)
                print("Result:", first, "*", second, "=", result)

            elif choice == "4":
                result = divide(first, second)
                if result is None:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result:", first, "/", second, "=", result)

            elif choice == "5":
                result = modulus(first, second)
                print("Result:", first, "%", second, "=", result)

            elif choice == "6":
                result = exponent(first, second)
                print("Result:", first, "**", second, "=", result)

        else:
            print("Invalid choice. Please try again.")

main()