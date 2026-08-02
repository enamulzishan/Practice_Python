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

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break
    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid input. Please enter a number between 1 and 8.")
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
    else:
        print("Invalid input. Please enter a number between 1 and 8.")