import random

secret_number = random.randint(1,100)
max_attempts = 5
attempts = 1

victory_messages = [
    "WOW You got it first try WHAT A LEGEND!",
    "Great, you got it in 2 attempts.",
    "Nice, you got it in 3 attempts.",
    "OK, you got it in 4 attempts. Cool",
    "Holy Smokes! Finally you got it correct in 5 attempts. DAMN!"
]

while attempts <= max_attempts:
    try:
        guess = int(input(f"Whats your guess #{attempts}?  "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if (guess == secret_number):
        print(victory_messages[attempts-1])
        print("Thanks for Playing!")
        break

    elif (guess<secret_number):
        print("Your guess is lower. Try Again!")
    else:
        print("Your guess is higher. Try Again!")

    attempts+=1

if (attempts>max_attempts):
    print("\nDamn, this was your final try.")
    print("Thats about it Dude, you could not guess the number.")
    print(f"FYI, the number was {secret_number}")
    print("Thanks for Playing!")


