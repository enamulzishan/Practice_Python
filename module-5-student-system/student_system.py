print("Welcome to Smart Student Life Management System")

s_name = input("Enter your name: ")
s_id = int(input("Enter your student ID: "))
s_hours = float(input("Enter your daily study hours per day: "))
m_money = float(input("Enter your monthly pocket money: "))

while True:
    print("\nMenu:")
    print("1. Class Attendance Tracker")
    print("2.Study Session Manager")
    print("3. Exam Result Checker")
    print("4. Monthly Expense Tracker")
    print("5. Daily Problem Solver")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("\nClass Attendance Tracker")
        total_classes = int(input("Enter total number of classes: "))
        attended_classes = int(input("Enter number of classes attended: "))
        attendance_percentage = (attended_classes / total_classes) * 100
        print(f"Your attendance percentage is: {attendance_percentage:.2f}%")
        if attendance_percentage >= 75:
            print("You are eligible for the exam.")
        else:
            print("You are not eligible for the exam.")

    elif choice == '2':
        print("\nStudy Session Manager")
        subject_name = input("Enter the subject name: ")
        no_of_study_sessions = float(input("Enter the number of study sessions you want to have today: "))
        no_of_study_sessions = int(no_of_study_sessions)
        for i in range(1, no_of_study_sessions + 1):
            print(f"Study Session {i} Completed")
            
        completed = input("Did you complete all sessions? (yes/no): ")
        if completed == 'yes':
            print("Great consistency!")
        else:
            print("Try to improve tomorrow.")

    elif choice == '3':
        print("\nExam Result Checker")
        python = float(input("Enter Python marks: "))
        math = float(input("Enter Mathematics marks: "))
        english = float(input("Enter English marks: "))
        
        total = python + math + english
        average = total / 3
        
        if average >= 80:
            last_grade = "A+"
        elif average >= 70:
            last_grade = "A"
        elif average >= 60:
            last_grade = "B"
        elif average >= 50:
            last_grade = "C"
        elif average >= 40:
            last_grade = "D"
        else:
            last_grade = "F"
            
        print(f"Total Marks: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {last_grade}")

    elif choice == '4':
        print("\nMonthly Expense Tracker")
        food = float(input("Enter Food expense: "))
        internet = float(input("Enter Internet expense: "))
        transport = float(input("Enter Transport expense: "))
        other = float(input("Enter Other expense: "))
        
        total_expense = food + internet + transport + other
        remaining_balance = m_money - total_expense
        
        print(f"Total expense: {total_expense}")
        print(f"Remaining pocket money: {remaining_balance}")
        
        if total_expense > m_money:
            print("Budget Limit Crossed.")
        else:
            print("You managed your expenses well.")

    elif choice == '5':
        print("\nDaily Problem Solver")
        print("1. Even or Odd Checker")
        print("2. Largest Number Finder")
        print("3. Simple Sum Calculator")
        
        sub_choice = input("Enter your choice (1-3): ")
        
        if sub_choice == '1':
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print("Even")
            else:
                print("Odd")
                
        elif sub_choice == '2':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            num3 = float(input("Enter 3rd number: "))
            
            if num1 >= num2 and num1 >= num3:
                print(f"Largest number is {num1}")
            elif num2 >= num1 and num2 >= num3:
                print(f"Largest number is {num2}")
            else:
                print(f"Largest number is {num3}")
                
        elif sub_choice == '3':
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            print(f"Total sum: {num1 + num2}")

    elif choice == '6':
        print("\nCountdown Timer")
        count = int(input("Enter a countdown number: "))
        
        while count > 0:
            print(count)
            count = count - 1
            
        print("Session Finished Successfully.")
        
        print("\n========== FINAL SUMMARY ==========")
        print(f"Student Name: {s_name}")
        print(f"Student ID: {s_id}")
        print("\nThank You For Using The System.")
        break