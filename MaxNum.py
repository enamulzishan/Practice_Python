print("What is the maximum number in 3 numbers?")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
  print(f"The maximum number is: {a}")
elif b >= a and b >= c:
  print(f"The maximum number is: {b}")
else:
  print(f"The maximum number is: {c}")