print("Welcome to Daily Life Tracker Program")

name = input('What is your name? :')
print(f"Hello, {name}!")
hours = float(input('How many hours available today? :'))
budget = float(input('What is your budget for today? :'))

study_hours = float(input('How many hours do you want to study today? :'))
practice_hours = float(input('How many hours do you want to practice today? :'))
other_hours = float(input('How many hours do you want to spend on other activities today? :'))

total_hours = study_hours + practice_hours + other_hours

print("Total activity hours planned for the day :", total_hours)


food_expense = float(input('How much do you plan to spend on food today? :'))
transport_expense = float(input('How much do you plan to spend on transport today? :'))
other_expense = float(input('How much do you plan to spend on other expenses today? :'))
total_expense = food_expense + transport_expense + other_expense
print("Total daily expense :", total_expense)

if total_hours > hours:
    print("You have planned more hours than available.")
else:    print("Your daily plan is realistic.")

if total_expense > budget:
    print("You have exceeded your daily budget.")
else:    print("You are within your daily budget.")