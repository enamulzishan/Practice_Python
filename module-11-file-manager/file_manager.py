print("Welcome to Smart File-Based Manager")

import random
import os
import csv
import datetime

while True:
  print("\n1.Add new expense")
  print("2.View all expenses")
  print("3.Add new note")
  print("4.View all notes")
  print("5.Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    expense = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))

    with open("E:\\OSTAD\\module-11-file-manager\\expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([random.randint(1, 1000), expense, amount, datetime.datetime.now()])

  elif choice == '2':
    if os.path.exists("E:\\OSTAD\\module-11-file-manager\\expenses.csv"):
      with open("E:\\OSTAD\\module-11-file-manager\\expenses.csv", "r") as file:
        reader = csv.reader(file)
        found = False

        for row in reader:
          found = True
          print(f"ID: {row[0]} | Title: {row[1]} | Amount: {row[2]} | Date: {row[3]}")

        if not found:
          print("No records found yet.")
    else:
      print("No records found yet.")

  elif choice == '3':
    note = input("Enter note title: ")
    content = input("Enter note content: ")

    with open("E:\\OSTAD\\module-11-file-manager\\notes.txt", "a") as file:
        file.write(f"{random.randint(1, 1000)},{note},{content},{datetime.datetime.now()}\n")

  elif choice == '4':
    if os.path.exists("E:\\OSTAD\\module-11-file-manager\\notes.txt"):
      with open("E:\\OSTAD\\module-11-file-manager\\notes.txt", "r") as file:
        found = False

        for line in file:
          found = True
          row = line.strip().split(",")
          print(f"ID: {row[0]} | Title: {row[1]} | Content: {row[2]} | Date: {row[3]}")

        if not found:
          print("No records found yet.")
    else:
      print("No records found yet.")

  elif choice == '5':
    break