print("Fibonacci Sequence Generator")
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    