import random

def play_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100. Try again!")
            elif guess < target:
                print("Too low! Here's a hint: The number is greater than", guess)
            elif guess > target:
                print("Too high! Here's a hint: The number is less than", guess)
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts. The number was {target}.")
                break
        except ValueError:
            print("That's not a valid number! Please enter a number between 1 and 100.")

def main():
    while True:
        play_guessing_game()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
