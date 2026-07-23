print("Welcome to Smart School Management & Voting Analysis System")

Names = []
Scores = []
contacts = {}


while True:
  print("1. Add Student Scores")
  print("2. View Score Summary")
  print("3. Manage Contacts/Inventory")
  print("4. Run Voting System")
  print("5. Searching Features")
  print("6. Exit")
  choice = input("Enter your choice (1-6): ")
  if choice == '1':
    # Add Student Scores
    print("Adding Student Scores...")
    students = int(input("How many students to enter scores for? "))
    for i in range(students):
        name = input(f"Enter the name of student {i + 1}: ")
        score = float(input(f"Enter the score of student {i + 1}: "))
        Names.append(name)
        Scores.append(score)

    print("Names", Names)
    print("Scores", Scores)
    print("\nStudent Score List")
    for i in range(len(Names)):
        print(f"{Names[i]} : {Scores[i]}")

    score_tuple = tuple(Scores)
    print("Scores as Tuple:", score_tuple)
    try:
        score_tuple[0] = 100
    except TypeError:
        print("Cannot modify tuple, it is immutable.")

  elif choice == '2':
     print("Viewing Score Summary...")
     if len(Scores) > 0:
        max_score = Scores[0]
        min_score = Scores[0]
        average_score = 0
        total_score = 0
        for s in Scores:
            if s > max_score:
                max_score = s
            if s < min_score:
                min_score = s
            total_score += s
        average_score = total_score / len(Scores)
        print(f"Maximum Score: {max_score}")
        print(f"Minimum Score: {min_score}")
        print(f"Average Score: {average_score}")
     else:
        print("No scores available to summarize.")

       
  elif choice == '3':
    print("Managing Contacts/Inventory...")
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Update Contact")
        print("5. Back to Main Menu")

        sub_choice = input("Enter your choice (1-5): ")

        if sub_choice == '1':
            contact = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")

            contacts[contact] = phone
            print("Contacts:", contacts)

        elif sub_choice == '2':
            contact = input("Enter contact name to delete: ")

            if contact in contacts:
                del contacts[contact]
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif sub_choice == '3':
            print("Contacts:", contacts)

        elif sub_choice == '4':
            contact = input("Enter contact name to update: ")
            if contact in contacts:
                phone = input("Enter new phone number: ")
                contacts[contact] = phone
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif sub_choice == '5':
            break

        else:
            print("Invalid choice!")

        for name, phone in contacts.items():
         print(name, "->", phone)

  elif choice == '4':
    print("Running Voting System...")
    votes = []
    vote_count = {}

    voters = int(input("Enter number of voters: "))

    for i in range(voters):
        vote = input(f"Enter vote of voter {i+1}: ")
        votes.append(vote)

    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

    print("Vote Results:")
    for candidate in vote_count:
        print(candidate, ":", vote_count[candidate])

    winner = ""
    highest = 0

    for candidate in vote_count:
        if vote_count[candidate] > highest:
            highest = vote_count[candidate]
            winner = candidate

    print("Winner is", winner)

  elif choice == '5':
    print("Searching Features...")

    print("1. Search Student")
    print("2. Search Contact")
    print("3. Search Candidate")

    search_choice = input("Enter your choice (1-3): ")

    if search_choice == '1':
        student = input("Enter student name: ")

        if student in Names:
            index = Names.index(student)
            print("Student:", Names[index])
            print("Score:", Scores[index])
        else:
            print("Record not found.")

    elif search_choice == '2':
        contact = input("Enter contact name: ")

        if contact in contacts:
            print(contact, ":", contacts[contact])
        else:
            print("Record not found.")

    elif search_choice == '3':
        candidate = input("Enter candidate name: ")

        if candidate in vote_count:
            print(candidate, "received", vote_count[candidate], "votes")
        else:
            print("Record not found.")

  elif choice == '6':
    print("Thank You for Using Smart School Management System.")
    break

  else:
    print("Invalid choice! Please try again.")


    categories = set()

    total = int(input("How many categories do you want to add? "))

    for i in range(total):
        category = input(f"Enter category {i+1}: ")
        categories.add(category)

    print("Unique Categories:", categories)

    another_set = set()

    total2 = int(input("How many categories for another set? "))

    for i in range(total2):
        category = input(f"Enter category {i+1}: ")
        another_set.add(category)

    print("Second Set:", another_set)

    union_set = categories.union(another_set)
    difference_set = categories.difference(another_set)

    print("Union:", union_set)
    print("Difference:", difference_set)

    
    student_marks = {
        "John": [80, 75, 90],
        "Alex": [70, 85, 88]
    }

    for student in student_marks:
        print("\nStudent Name:", student)

        total = 0

        print("Subject Scores:")

        for mark in student_marks[student]:
            print(mark)
            total = total + mark
print("Total Score:", total)