print("how many even and odd numbers are in a list?")

numbers = [1,2,3,4,5,6,7,8,9,10,11,11,12,13]
count = {"even": 0, "odd": 0}
for n in numbers:
    if n % 2 == 0:
        count["even"] += 1
    else:
        count["odd"] += 1

print(f"Even numbers: {count['even']}")
print(f"Odd numbers: {count['odd']}")