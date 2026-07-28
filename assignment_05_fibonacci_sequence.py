def print_fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be greater than 0.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term

    print()

def check_fibonacci(number):
    first = 0
    second = 1

    while first < number:
        next_term = first + second
        first = second
        second = next_term

    if first == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")

def main():
    n = int(input("How many terms? "))
    print_fibonacci(n)

    number = int(input("Enter a number to check: "))
    check_fibonacci(number)

main()