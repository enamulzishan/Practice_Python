print('Welcome to Smart Eligibility & Performance Checker')
name = input('Enter your name :')
age = float(input('Enter your age :'))
exam_score = float(input('Enter your exam score :'))
monthly_income = float(input('Enter your monthly income :'))
if age <18:
  print('You are not eligible due to age restrictions.')
else:
  print('Age requirement passed.')

if exam_score >=90:
  print("Grade: A")
elif exam_score >=75:
  print("Grade: B")
elif exam_score >=60:
  print("Grade: C")
else:  print("Grade: F")

if monthly_income < 20000 and exam_score >= 75:
  print('Eligible for schoolarship support.')
else: print('Not eligible for schoolarship support.')

if age >= 18:
  if exam_score >=60:
    print('You passed the program.')
  else: print('You failed the program.')
else: 
  print('Program access denied.')