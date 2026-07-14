print("Welcome to Smart Daily Helper Toolkit")
while True:

  age_years = float(input(' Enter your age in years :'))
  months = age_years*12
  print(f'Your age in months is {months}')

  age = float(input('Enter your age :'))

  if age>=18:
    print('Your are eligible to vote.')
  else: 
    print('Your are not eligible to vote')

  num1 = float(input('Enter your first number:'))
  num2 = float(input('Enter your second number:'))
  num3 = float(input(' Enter your third number:'))
  
  if num1< num2 and num1< num3:
    print('The smallest number is :', num1)
  elif num2< num1 and num2< num3:
    print('The smallest number is :', num2)
  else:
    print('The smallest number is :', num3)

  choice = input('Do you want to solve another problem? (yes/no) :')
  if choice.lower() == 'yes':
    continue
  else:  print('Thank you for using Smart Daily Helper Toolkit. Goodbye!')
  break

celsius = float(input('Enter temperature in Celsius :'))
fahrenheit = (celsius * 9/5) + 32
print(f'Temperature in Fahrenheit is : {fahrenheit}')