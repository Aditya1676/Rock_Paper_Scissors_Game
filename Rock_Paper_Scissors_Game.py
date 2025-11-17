import random

print("=== Rock Paper Scissors Game ===")

choices = ["rock", "paper", "scissors"]

while True:
    print("\n--- New Round ---")
    user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

    if user == "q":
        print("Game ended. Thanks for playing!")
        break

    if user not in choices:
        print("Invalid input! Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("Result: It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You win!")
    else:
        print("Result: You lose!")

