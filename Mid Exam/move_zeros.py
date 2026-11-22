
number = [int(x) for x in input("Enter the number list (space-separated): ").split()]
zeros = number.count(0)
non_zeros = []
for x in number:
    if x != 0:
        non_zeros.append(x)
list_numbers = non_zeros + [0] * zeros
print("List after moving zeros to the end:", list_numbers)
