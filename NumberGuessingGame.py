import random

print("***This is a number guessing game.***")
print("**Guess a number between 0 and 100!**")

num = random.randint(0, 100)

attempts = 1
Guess = 0
while(Guess != num):
    try:
        Guess = int(input("Enter your guess:"))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if(Guess>num):
        print("TOO HIGH!, Guess lower.")
        attempts = attempts + 1
    elif(Guess<num):
        print("TOO LOW!, Guess higher.")
        attempts = attempts + 1
    elif(Guess == num):
        print(f"You guessed correct!, It took You {attempts} Tries!")
