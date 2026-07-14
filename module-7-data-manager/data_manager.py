print("Welcome to Smart Contact & Inventory Manager")

contacts = {}
con_add = int(input("how many contacts you want to add: "))

for i in range(con_add):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
for name, phone in contacts.items():
    print(f"{name} - {phone}")

first_name = input("Enter first name to search: ")
if first_name in contacts:
    print(f"Contact found: {first_name} - {contacts[first_name]}")
else:
    print("Contact not found.")
name_update = input("Enter contact name to update: ")
if name_update in contacts:
    new_phone = input("enter new phone number:")
    contacts[name_update] = new_phone
    print("Contact updated successfully.")
name_delete = input("Enter contact name to delete: ")
if name_delete in contacts:
    del contacts[name_delete]
    print("Contact deleted successfully.")

categories = {"Electronics", "Clothing", "Books", "Sports", "Others"}
category = input(f"Enter product category {categories}: ")

another_categories = {"food", "eggs", "others"}

all_categories = categories.union(another_categories)
print("All categories:", all_categories)
difference_categories = categories.difference(categories)
print("difference_categories:", difference_categories)

products = {
"Laptop": {"price": 50000, "stock": 10},
"Phone": {"price": 30000, "stock": 20}
}
product_name = input("Enter product name to search: ")
if product_name in products:
    print(f"Product found: {product_name} - Price: {products[product_name]['price']}, Stock: {products[product_name]['stock']}")
else:
    print("Product not found.")