# ============================================
# Synent Technologies - Python Internship
# Task 2: Number Guessing Game (CLI)
# Developer: Lincoln Adura
# ============================================

import random

def number_guessing_game():
    print("=" * 40)
    print("  Synent Technologies - Guessing Game")
    print("=" * 40)
    print("\nI'm thinking of a number between 1 and 100!")
    print("Can you guess it?\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1
                continue

            if guess < secret_number:
                print(f"Too low! Try higher. (Attempt {attempts})")
            elif guess > secret_number:
                print(f"Too high! Try lower. (Attempt {attempts})")
            else:
                print("=" * 40)
                print(f"🎉 Correct! The number was {secret_number}!")
                print(f"You got it in {attempts} attempts!")
                print("=" * 40)
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    number_guessing_game()