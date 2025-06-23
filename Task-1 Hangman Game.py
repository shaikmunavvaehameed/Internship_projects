import random

# Predefined list of 5 words
word_list = ["apple", "banana", "grape", "orange", "mango"]

# Select a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
tries = 6

# Create a display version of the word
display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while tries > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Correct!\n")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} incorrect guesses left.\n")

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you're out of tries. The word was:", secret_word)
