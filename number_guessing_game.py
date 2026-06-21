from random import randint

def play_game():
    print("\nChoose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    while True:
        choice = input("Enter difficulty (1/2/3): ")

        if choice == "1":
            max_number = 50
            break
        elif choice == "2":
            max_number = 100
            break
        elif choice == "3":
            max_number = 500
            break
        else:
            print("Please choose from 1, 2, or 3.")

    # Generate a random number within the selected range
    secret_number = randint(1, max_number)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if (guess < 1) or (guess > max_number):
            print(f"Please enter a number between 1 and {max_number}.")
            continue

        attempts += 1

        if (guess > secret_number):
            print("Lower number please.")
        elif (guess < secret_number):
            print("Higher number please.")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return attempts


print("=" * 30)
print("     NUMBER GUESSING GAME")
print("=" * 30)

best_score = None

while True:
    attempts = play_game()

    # Update best score if a better score is achieved
    if best_score is None or (attempts < best_score):
        best_score = attempts
        print(f"New Best Score: {best_score} attempts!")
    else:
        print(f"Best Score: {best_score} attempts")

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing!")
        break