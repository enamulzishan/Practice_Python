amount = int(input("Enter amount: "))
member = input("are you a member? (yes/no): ")

if amount <= 0:
    print("Invalid amount")

elif amount >= 5000:
    discount = 20

elif amount >= 2500:
    discount = 10

else:
    discount = 0

if amount > 0:
    if member == "yes":
        discount += 5

    total_discount = amount * discount / 100
    final_amount = amount - total_discount

    print("Discount:", discount, "%")
    print("Discount Amount:", total_discount)
    print("Final Amount:", final_amount)