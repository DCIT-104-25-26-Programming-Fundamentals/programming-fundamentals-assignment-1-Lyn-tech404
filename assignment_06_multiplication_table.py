def single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def all_tables(n):
    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
        print("---------------------------")

def main():
    number = int(input("Enter a number: "))
    single_table(number)

    n = int(input("Enter a number: "))

    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    all_tables(n)

main()