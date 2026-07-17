print("Welcome to Smart Task Repetition System")

task_name = input("Enter your task name: ")
task_count = int(input("How many times do they want to repeat this task today: "))

for i in range(task_count):
    print(f"Task( {i+1}): Study {task_name} completed.")

countdown = int(input("Enter the countdown number: "))

while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

print("Countdown finished!")

print("Daily Schedule")

sessions = ["Morning", "Evening"]

for session in sessions:
    for i in range(1, 4):
        print(f"{session} Session {i}: Study {task_name}")


while True:
    print("this loop will run forever !!!")
    