app_name = "Smart Calculator"


def display_app_name():
    print("Application Name:", app_name)


display_app_name()
print("Welcome to Smart Calculator")


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
def floor_division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b
def percent(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return (a / b) * 100
def square_root(a):
    if a < 0:
        return "Error: Square root of negative number is not defined."
    return a ** 0.5
def cube(a):
    return a ** 3
def cube_root(a):
    if a < 0:
        return -(-a) ** (1/3)
    return a ** (1/3)
def maximum(a, b):
    return max(a, b)
def minimum(a, b):
    return min(a, b)

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Percent")
    print("9. Square Root")
    print("10. Cube")
    print("11. Cube Root")
    print("12. Maximum")
    print("13. Minimum")
    print("14. Exit")

    choice = input("Enter choice (1-14): ")

    if choice == '14':
        print("Exiting the calculator. Goodbye!")
        break
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
        print("Invalid input. Please enter a number between 1 and 14.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == '5':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")
    elif choice == '7':
        result = floor_division(num1, num2)
        print(f"{num1} // {num2} = {result}")
    elif choice == '8':
        result = percent(num1, num2)
        print(f"{num1} is {result}% of {num2}")
    elif choice == '9':
        result = square_root(num1)
        print(f"Square root of {num1} is {result}")
    elif choice == '10':
        print(f"Cube of {num1} is {cube(num1)}")
    elif choice == '11':
        result = cube_root(num1)
        print(f"Cube root of {num1} is {result}")
    elif choice == '12':
        print(f"Maximum of {num1} and {num2} is {maximum(num1, num2)}")
    elif choice == '13':
        print(f"Minimum of {num1} and {num2} is {minimum(num1, num2)}")
    else:
        print("Invalid input. Please enter a number between 1 and 14.")



square = lambda number: number ** 2
square_number = float(input("Enter a number to find its square: "))
print(f"The square of {square_number} is {square(square_number)}")

numbers = [5, 10, 15, 20, 25]
increased_numbers = list(map(lambda number: number + 10, numbers))
print(increased_numbers)

filtered_numbers = list(filter(lambda number: number > 15, numbers))
print(filtered_numbers)
