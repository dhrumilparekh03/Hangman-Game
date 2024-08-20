import random

def choose_word():
    # List of words for the game
    words = ['python', 'hangman', 'programming', 'challenge', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    word_length = len(word)
    max_incorrect_guesses = word_length

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses and set(word) != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print(display_word(word, guessed_letters))
    
    if set(word) == guessed_letters:
        print(f"Congratulations! You guessed the word '{word}' correctly.")
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
