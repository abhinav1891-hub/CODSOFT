# Rock Paper Scissors Game
# CodSoft Internship Task

import random

print("===== Rock Paper Scissors Game =====")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win! 🎉")
        user_score += 1

    else:
        print("Computer wins! 🤖")
        computer_score += 1

    # Show score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break