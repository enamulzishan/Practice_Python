print("Welcome to Smart Voting & Student Management System")

# Voting Data Input
votes = []
voter = int(input("how many voters will vote :"))

for i in range(voter):
    name = input ("Enter your name: ")
    votes.append(name)

frequency = {}
for name in votes:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1
        
print("Voting Results:")
for name, count in frequency.items():
    print(f"{name}: {count} votes")

winner = max(frequency, key=frequency.get)
print(f"The winner is: {winner} with {frequency[winner]} votes")

search_name = input("Enter the name to search for: ")
if search_name in frequency:
    print(f"{search_name} received {frequency[search_name]} votes.")
else:
    print(f"{search_name} was not found in the voting results.")