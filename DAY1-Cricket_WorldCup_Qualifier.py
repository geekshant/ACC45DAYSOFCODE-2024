# Input: total points scored by the team (within the constraints)
X = int(input("Enter the total points scored by the team (1-20): "))

# Check if the team has qualified
if 1 <= X <= 20:
    if X >= 12:
        print("Yes")
    else:
        print("No")
# this line of code prints (invalid) if user do not enter the correct value of points (X)
else:
    print("Invalid input. Points should be between 1 and 20.")
