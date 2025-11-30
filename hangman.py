import random

words = ["apple", "tiger", "chair", "water", "phone"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already used this letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
