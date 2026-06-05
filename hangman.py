import random

# List of predefined words
words = ["python", "apple", "laptop", "coding", "school"]

# Maximum incorrect attempts
MAX_ATTEMPTS = 6


def display_word(word, guessed_letters):
    """Display guessed letters and underscores for remaining letters."""
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def play_hangman():
    # Randomly choose a word
    word = random.choice(words)

    guessed_letters = []
    attempts = MAX_ATTEMPTS

    print("=" * 50)
    print("🎮 WELCOME TO HANGMAN GAME")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts.")
    print("=" * 50)

    while attempts > 0:

        # Show current progress
        current_word = display_word(word, guessed_letters)
        print("\nWord:", current_word)

        # Check if player has guessed all letters
        if "_" not in current_word:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            break

        # Take input
        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter only ONE alphabet letter.")
            continue

        # Check duplicate guesses
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        # Store guessed letter
        guessed_letters.append(guess)

        # Check guess
        if guess in word:
            print("✅ Correct Guess!")
        else:
            attempts -= 1
            print("❌ Wrong Guess!")
            print("Remaining Attempts:", attempts)

    # If attempts become 0
    if attempts == 0:
        print("\n💀 GAME OVER!")
        print("The correct word was:", word)


# Start the game
if __name__ == "__main__":
    play_hangman()